from numpy import ndarray as np_ndarray, zeros as np_zeros, mean as np_mean, newaxis as np_newaxis, sum as np_sum, argmin as np_argmin

def calculate_centers(data: np_ndarray, cluster_assignments: np_ndarray, k: int) -> np_ndarray:
    n_features = data.shape[1]
    new_centroids = np_zeros((k, n_features))
    
    for cluster_id in range(k):
        cluster_mask = cluster_assignments == cluster_id
        cluster_points = data[cluster_mask]
        
        if len(cluster_points) > 0:
            new_centroids[cluster_id] = np_mean(cluster_points, axis=0)
    
    return new_centroids

def assign_clusters(data: np_ndarray, centroids: np_ndarray) -> np_ndarray:
    differences = data[:, np_newaxis, :] - centroids[np_newaxis, :, :]
    squared_distances = np_sum(differences ** 2, axis=2)
    cluster_assignments = np_argmin(squared_distances, axis=1)
    return cluster_assignments
