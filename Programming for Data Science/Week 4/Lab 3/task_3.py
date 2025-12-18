from load import load_and_separate_dataframes_as_arrays
from time import perf_counter as time_perf_counter
from task_3_display import display_results
from numpy import ndarray as np_ndarray
from data_types import Task3Results
from task_3_kmeans import kmeans

def task_3(
    features_array: np_ndarray = None,
    show_results: bool = False,
    k: int = None,
) -> Task3Results:
    if features_array is None:
        load_and_separate_dataframes_as_arrays_results = load_and_separate_dataframes_as_arrays()
        features_array = load_and_separate_dataframes_as_arrays_results.features

    if k is None:
        k = int(input("Enter the number of clusters (k): "))

    start_time = time_perf_counter()
    cluster_assignments, final_centroids = kmeans(data=features_array, k=k)
    end_time = time_perf_counter()
    execution_time = end_time - start_time

    if show_results:
        display_results(
            cluster_assignments=cluster_assignments,
            final_centroids=final_centroids,
            execution_time=execution_time,
            data=features_array,
            k=k,
        )

    return Task3Results(
        cluster_assignments=cluster_assignments,
        final_centroids=final_centroids,
        execution_time=execution_time,
        features=features_array,
        k=k,
    )

if __name__ == "__main__":
    task_3(show_results=True)