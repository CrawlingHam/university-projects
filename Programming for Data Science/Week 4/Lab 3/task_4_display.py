from data_types import KMeansSklearnResults, KNNSklearnResults, Task3Results, Results
from numpy import array as np_array

def display_results(
    kmeans_scikit_learn_results: KMeansSklearnResults,
    knn_scikit_learn_results: KNNSklearnResults,
    kmeans_task_results: Task3Results,
    knn_vectorized_results: Results,
    knn_iterative_results: Results,
) -> None:
    print("\nKNN Results:")

    print(f"\nIterative execution time: {knn_iterative_results.execution_time * 1000:.6f} milliseconds")
    print(f"Iterative predictions accuracy: {knn_iterative_results.accuracy:.4f} ({knn_iterative_results.accuracy*100:.2f}%)")

    print(f"\nVectorized execution time: {knn_vectorized_results.execution_time * 1000:.6f} milliseconds")
    print(f"Vectorized predictions accuracy: {knn_vectorized_results.accuracy:.4f} ({knn_vectorized_results.accuracy*100:.2f}%)")

    print(f"\nScikit-Learn execution time: {knn_scikit_learn_results.execution_time * 1000:.6f} milliseconds")
    print(f"Scikit-Learn predictions accuracy: {knn_scikit_learn_results.accuracy:.4f} ({knn_scikit_learn_results.accuracy*100:.2f}%)")

    print(f"\nSpeedup Vectorized vs Iterative: {knn_iterative_results.execution_time / knn_vectorized_results.execution_time:.2f}x")
    print(f"Speedup Vectorized vs Scikit-Learn: {knn_scikit_learn_results.execution_time / knn_vectorized_results.execution_time:.2f}x")
    print(f"Speedup Scikit-Learn vs Iterative: {knn_iterative_results.execution_time / knn_scikit_learn_results.execution_time:.2f}x")

    print("\nK-Means Results:")

    print(f"\nVectorized execution time: {kmeans_task_results.execution_time * 1000:.6f} milliseconds")
    vectorized_clusters_array = np_array(kmeans_task_results.cluster_assignments)
    vectorized_centroids_array = np_array(kmeans_task_results.final_centroids)
    print(f"Vectorized clusters: {vectorized_clusters_array}")
    print(f"Vectorized centroids: {vectorized_centroids_array}")

    print(f"\nScikit-Learn execution time: {kmeans_scikit_learn_results.execution_time * 1000:.6f} milliseconds")
    sklearn_clusters_array = np_array(kmeans_scikit_learn_results.cluster_assignments)
    sklearn_centroids_array = np_array(kmeans_scikit_learn_results.final_centroids)
    print(f"Scikit-Learn clusters: {sklearn_clusters_array}")
    print(f"Scikit-Learn centroids: {sklearn_centroids_array}")

    print(f"\nSpeedup Vectorized vs Scikit-Learn: {kmeans_scikit_learn_results.execution_time / kmeans_task_results.execution_time:.2f}x")
