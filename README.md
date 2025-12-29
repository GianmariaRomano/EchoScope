# 🎵 EchoScope: Spotify Track Analysis & Recommendation System

## 🎧 About this repository

This repository contains a machine learning project that analyzes Spotify audio features to:
- Cluster songs based on musical characteristics
- Predict track popularity
- Build a content-based recommendation system

This project is based on the *Spotify Tracks Dataset* from Kaggle.

---

## 📊 Dataset

**Source:** *Spotify Tracks Dataset* from Kaggle

**Size:** ~114k tracks  

**Features include:**
- Acousticness
- Danceability
- Energy
- Loudness
- Tempo
- Valence
- Popularity
- Genre / Artist metadata

The dataset provides Spotify’s audio analysis features, making it suitable for clustering and predictive modeling.

---

## ⚙️ Pipeline

1. **Visualization & Preprocessing**
   - Feature distributions and correlation analysis
   - Handling missing values
   - Feature scaling & normalization

2. **Feature Clustering**
   - Visualization using PCA
   - Computations using K-Means
   - Evaluation using Silhouette Score
   - Cluster interpretation

3. **Popularity Prediction (Coming Soon)**
   - TBA

4. **Recommendation System (Coming Soon)**
   - TBA

5. **API Development (Coming Soon)**
   - TBA

---

## 🧠 Models & Techniques (To Update)

- **Clustering:** PCA, K-Means
- **Prediction:** TBA
- **Recommendations:** TBA
- **Evaluation:** Silhouette Score

---

## 📈 Results (Coming Soon)

- Setting a random seed equal to 26 using n_components = 2 and K = 5 gives groups that seem to overlap: for future analysis, the model could benefit from working with more components during the PCA steps and/or from using more clusters.
- TBA

---

## 🛠 Structure (To Update)

```html
<pre>
|-- data/
|   |-- dataset.csv
|   |-- dataset_clean.csv
|   `-- dataset_clustered.csv
|-- notebooks/
|   |-- data_visualization.ipynb
|   |-- data_preprocessing.ipynb
|   `-- clustering.ipynb
|-- src/
|   |-- preprocessing.py
|   `-- clustering.py
|-- LICENSE
`-- README.md
</pre>
```

---

## 📄 License

This project is released under the **MIT License**.

The dataset used in this project comes from Kaggle:
**Spotify Tracks Dataset** by Maharshi Pandya.  
The dataset is subject to Kaggle’s dataset licensing terms and is used here for educational and research purposes only.

Please refer to the dataset’s Kaggle page for full licensing details.
