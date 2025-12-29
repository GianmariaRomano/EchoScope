import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from preprocessing import load_data

def apply_pca(data, n_components):
    # Apply principal component analysis to perform dimensionality reduction.
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(scaled_data)
    return pca_data, pca, scaler

def cluster_data(pca_data, n_clusters):
    # Apply K-means and evaluate the returned clusters using the Sihlouette Score metric
    kmeans = KMeans(n_clusters=n_clusters, random_state=26)  # Apply a random seed for reproducibility.
    labels = kmeans.fit_predict(pca_data)
    silhouette = silhouette_score(pca_data, labels)
    return labels, kmeans, silhouette

def save_results(original_data, labels, output_file="clustered_data.csv"):
    # Save the dataset with the cluster labels as well.
    original_data['cluster'] = labels
    original_data.to_csv(output_file, index=False)
    print(f"Clustered data saved to {output_file}")