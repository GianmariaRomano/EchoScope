from fastapi import FastAPI, HTTPException
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# Start by creating the application.
app = FastAPI(
    title="EchoScope API",
    description="API for Analysing Patterns in Music",
    version="1.0.0"
)

# Loading the dataset.
DB_PATH = 'data/echoscope_production_data.csv' # Full path in the GitHub repository.
df = pd.read_csv(DB_PATH)

# Extracting the relevant features.
audio_features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 
                  'instrumentalness', 'liveness', 'valence', 'tempo']

# Pre-processing the dataset.
scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[audio_features] = scaler.fit_transform(df[audio_features])

# --- Endpoints ---

@app.get("/")
def read_root():
    return {
        "project": "EchoScope",
        "status": "Online",
        "endpoints": ["/search", "/recommend"]
    }

@app.get("/search")
def search_song(title: str):
    # Search songs in the dataset.
    results = df[df['track_name'].str.contains(title, case=False, na=False)].head(10)
    if results.empty:
        raise HTTPException(status_code=404, detail="Song Not Found")
    return results[['track_name', 'artists', 'album_name', 'popularity_pred']].to_dict(orient="records")

@app.get("/recommend")
def get_recommendations(track_name: str, artist_name: str = None, n: int = 5):
    # Create a playlist based on similarity and popularity prediction.    
    # Find the input song.
    mask = df_scaled['track_name'].str.contains(track_name, case=False, na=False)
    if artist_name:
        mask &= df_scaled['artists'].str.contains(artist_name, case=False, na=False)
    ref_matches = df_scaled[mask]
    if ref_matches.empty:
        raise HTTPException(status_code=404, detail="Input Song Not Found")
    song_ref = ref_matches.iloc[0]
    ref_cluster = song_ref['cluster']
    # Cluster-based filtering for better efficiency.
    candidates = df_scaled[df_scaled['cluster'] == ref_cluster].copy()
    # Compute the cosine similarity.
    similarities = cosine_similarity(
        [song_ref[audio_features]], 
        candidates[audio_features]
    ).flatten()
    candidates['similarity'] = similarities
    # Ranking score = 70% Cosine similarity + 30% popularity prediction. The score is then normalized to [0, 1].
    candidates['final_score'] = (candidates['similarity'] * 0.7) + ((candidates['popularity_pred'] / 100) * 0.3)
    # Final selection, excluding the input song.
    recommendations = candidates[candidates['track_name'] != song_ref['track_name']]
    recommendations = recommendations.sort_values(by='final_score', ascending=False).head(n)
    return {
        "base_song": {
            "title": song_ref['track_name'],
            "artist": song_ref['artists'],
            "cluster": int(ref_cluster)
        },
        "recommendations": recommendations[['track_name', 'artists', 'similarity', 'popularity_pred']].to_dict(orient="records")
    }