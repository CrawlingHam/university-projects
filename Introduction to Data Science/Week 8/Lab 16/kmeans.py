from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from pandas import DataFrame

cluster_std = 5.0
random_state = 42
n_samples = 300
n_features = 2
centers = 10

features, true_centers = make_blobs(
    random_state=random_state,
    cluster_std=cluster_std,
    n_features=n_features,
    n_samples=n_samples,
    centers=centers,
)

dataframe = DataFrame(features, columns=["x1", "x2"])

kmeans = KMeans(n_clusters=centers, random_state=random_state)
kmeans.fit(features)

cluster_predictions = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.figure(figsize=(7, 5))
plt.scatter(features[:,0], features[:,1], c=cluster_predictions, cmap="viridis", s=50)
plt.scatter(centroids[:,0], centroids[:,1], c="red", marker="X", s=200, label="Centroids")
plt.title("K-Means Clustering Results")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()