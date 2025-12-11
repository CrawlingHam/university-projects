from centers import calculate_centers, assign_clusters
from imports import *

def kmeans(data: np_ndarray, k: int, max_iterations: int = 100, tolerance: float = 1e-4) -> Tuple[np_ndarray, np_ndarray]:
    n_samples, _n_features = data.shape
    
    np_random.seed(42)
    random_indices = np_random.choice(n_samples, size=k, replace=False)
    centroids = data[random_indices].copy()
        
    for _iteration in range(max_iterations):
        cluster_assignments = assign_clusters(data, centroids)
        new_centroids = calculate_centers(data, cluster_assignments, k)
        
        centroid_changes = np_linalg.norm(new_centroids - centroids, axis=1)
        max_change = np_max(centroid_changes)
        
        if max_change < tolerance:
            break
        
        centroids = new_centroids
    
    return cluster_assignments, centroids