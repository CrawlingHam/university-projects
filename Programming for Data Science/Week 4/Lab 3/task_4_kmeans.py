from time import perf_counter as time_perf_counter
from data_types import KMeansSklearnResults
from numpy import ndarray as np_ndarray
from sklearn.cluster import KMeans

def kmeans_scikit_learn(data: np_ndarray, k: int) -> KMeansSklearnResults:
    start_time = time_perf_counter()

    sklearn_kmeans = KMeans(n_clusters=k, random_state=42)
    sklearn_clusters = sklearn_kmeans.fit_predict(data)
    sklearn_centroids = sklearn_kmeans.cluster_centers_
    
    sklearn_kmeans_time = time_perf_counter() - start_time
    
    return KMeansSklearnResults(
        cluster_assignments=sklearn_clusters.tolist(),
        final_centroids=sklearn_centroids.tolist(),
        execution_time=sklearn_kmeans_time,
        n_iter=sklearn_kmeans.n_iter_,
    )