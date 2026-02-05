# 🎶 EchoScope – Spotify Track Analysis & Recommendation System

Music streaming platforms rely heavily on data-driven systems to understand user preferences and song characteristics.

For this reason, **EchoScope** explores how machine learning can be applies to analyse Spotify tracks to map the musical universe through data.

In particular, this project aims to provide the following services:
- Grouping songs based on their main features.
- Predicting the popularity potential of a song.
- Generating song recommendations by balancing acoustic similarity with predicted commercial success.

---

## 📌 Project Overview

The project is structured as a modular pipeline as each notebook focuses on a specific task of the pipeline:
- **Audio Mapping:** Clustering tracks based on the main musical features.
- **Productive Analytics:** Evaluating popularity using a regression model based on a random forest.
- **Smart Discovery:** Implementing a hybrid song and playlist recommendation engine based on similarity and predicted success.

---

## 📊 Dataset

**Source:** [Kaggle – Spotify Tracks Dataset]([link](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)) by Maharshi Pandya.

**Size:** ~114,000 tracks

**Key Features:** `danceability`, `energy`, `loudness`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`.

---

## ⚙️ Project Pipeline

The repository is organized into five main notebooks:
1)  `data_visualization.ipynb`: Exploratory Data Analysis step to identify eventual patterns within the dataset.
2)  `data_preprocessing.ipynb`: Clearning the raw dataset by handling missing values and performing feature scaling.
3)  `clustering.ipynb`: Implementing **Principal Component Analysis** and **K-Means Clustering** to group songs into musical identikits based on their features.
4)  `popularity_prediction.ipynb`: Training a **Random Forest Regression** to predict track popularity scores and investigating feature importance for popularity.
5)  `song_recommendation.ipynb`: A recommendation engine based on **Cosine Similarity** that is filtered by cluster and weighted by predicted popularity.

---

## 🧠 Models & Techniques

- **Dimensionality Reduction:** Principal Component Analysis.
- **Clustering:** K-Means with Elbow Method and Silhouette Score.
- **Regression:** Random Forest Regressor.
- **Similarity Metrics:** Cosine Similarity.
- **Dynamic Threshodling:** Evaluate song popularity using popularity percentiles for each cluster.

---

## 📂 Project Structure

```html
<pre>
├── data/
│   ├── dataset.csv                      # Original raw data
│   └── echoscope_production_data.csv    # Processed data with clusters and predictions
├── notebooks/
│   ├── data_visualization.ipynb
│   ├── data_preprocessing.ipynb
│   ├── clustering.ipynb
│   ├── popularity_prediction.ipynb
│   └── song_recommendation.ipynb
├── main.py                              # FastAPI application script
├── requirements.txt                     # Project dependencies
├── LICENSE
└── README.md
</pre>
```

---

## 🚀 Running the Project

1) Clone the repository:

```bash
git clone https://github.com/yourusername/echoscope.git
cd echoscope
```
2) Install the needed dependencies:

```bash
pip install -r requirements.txt
```
3) Run the pipeline.

---

## 🛰 Running the API

The EchoScope project includes a production-ready REST API built with **FastAPI** that allows to search for tracks and get real-time song recommendations.

To use the API:
1. Ensure you have installed all dependencies:
    ```bash
    pip install -r requirements.txt
    pip install uvicorn
    ```

2. Run the following command in your terminal, in the same directory as the `main.py` file:
    ```bash
    uvicorn main:app --reload
    ```

3. Once the server is running, visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

   Here, you will be able to use the `/search` endpoint to search for songs in the database and the `/recommend` enpoint to find similar songs to an input-provided song title.

---

## 🍪 API Usage Examples

### 🔍 1. Search Endpoint (`/search`)
Use this to find track metadata and confirm the exact name of a song in the database.

| Parameter | Type | Example Value | Description |
| :--- | :--- | :--- | :--- |
| **title** | `string` | `Primadonna` | The name of the track to search for |

**Example Response:**
```json
{
  "track_name": "Primadonna",
  "artists": "MARINA",
  "album_name": "Electra Heart (Deluxe)",
  "popularity_pred": 43.32
}
```

### 🎵 2. Recommendation Endpoint (`/recommend`)
The core engine, which is tasked with identifying the track's cluster and generating a list of recommendations based on audio similarity and popularity potential.

| Parameter | Type | Example Value | Description |
| :--- | :--- | :--- | :--- |
| **track_name** | `string` | `Flamingo` | Target song for similarity analysis |
| **artist_name**| `string` | `Kenshi Yonezu` | (Optional) To filter specific artists |
| **n** | `int` | `5` | Number of recommendations to return |

**Example Response:**
```json
{
  "base_song": {
    "title": "Flamingo",
    "artist": "Kenshi Yonezu",
    "cluster": 3
  },
  "recommendations": [
    {
      "track_name": "Potion (with Dua Lipa & Young Thug)",
      "artists": "Calvin Harris;Dua Lipa;Young Thug",
      "similarity": 0.99,
      "popularity_pred": 65.54
    },
    {
      "track_name": "Super Freaky Girl",
      "artists": "Nicki Minaj",
      "similarity": 0.98,
      "popularity_pred": 65.63
    },
    {
      "track_name": "Junio",
      "artists": "Maluma",
      "similarity": 0.99,
      "popularity_pred": 61.24
    },
    {
      "track_name": "Mañana",
      "artists": "Ozuna",
      "similarity": 0.98,
      "popularity_pred": 63.98
    },
    {
      "track_name": "One Kiss (with Dua Lipa)",
      "artists": "Calvin Harris;Dua Lipa",
      "similarity": 0.97,
      "popularity_pred": 66.99
    }
  ]
}
```

---
