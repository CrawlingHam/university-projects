from imports import *

def display_results(data: np_ndarray, execution_time: float, k: int, cluster_assignments: np_ndarray, final_centroids: np_ndarray) -> None:
    print("\nInformation:")
    print(f"Data points (rows): {data.shape[0]}")
    print(f"Features (columns): {data.shape[1]}")

    print("\nResults:")
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Number of clusters: {k}")
    print(f"Number of data points: {len(cluster_assignments)}")

    print("\nCluster sizes:")
    unique, counts = np_unique(cluster_assignments, return_counts=True)
    for cluster_id, count in zip(unique, counts):
        print(f"  Cluster {cluster_id}: {count} points ({count/len(cluster_assignments)*100:.1f}%)")

    print("\nFinal centroids:")
    feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    for i, centroid in enumerate(final_centroids):
        print(f"  Cluster {i}:")
        for j, feature_name in enumerate(feature_names):
            print(f"    {feature_name}: {centroid[j]:.4f}")

    print("=" * 60)
