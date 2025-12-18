from task_2_distance import distance_between_points as distance_vectorized
from task_1_evaluate import knn_predict, calculate_accuracy
from task_1 import prepare_dataframes, task_1
from data_types import Task2Results, Results
from task_2_display import display_results
from time import perf_counter as time_time

def task_2(
        train_features: list[list[float]] = None,
        test_features: list[list[float]] = None,
        train_labels: list[str] = None,
        test_labels: list[str] = None,
        show_results: bool = False,
        k: int = None,
    ) -> Task2Results:
    if train_features is None or train_labels is None or test_features is None or test_labels is None or k is None:
        prepare_dataframes_results = prepare_dataframes()
        train_features = prepare_dataframes_results.train_features
        test_features = prepare_dataframes_results.test_features
        train_labels = prepare_dataframes_results.train_labels
        test_labels = prepare_dataframes_results.test_labels
        k = prepare_dataframes_results.k

    results_iterative = task_1(train_features, test_features, train_labels, test_labels, k=k)
    time_iterative = results_iterative.execution_time

    start_time = time_time()
    predictions_vectorized = knn_predict(test_features, train_features, train_labels, k, distance_vectorized)
    end_time = time_time()
    time_vectorized = end_time - start_time
    
    accuracy_vectorized = calculate_accuracy(predictions_vectorized, test_labels)

    if show_results:
        display_results(
            predictions=predictions_vectorized,
            time_vectorized=time_vectorized,
            time_iterative=time_iterative,
            accuracy=accuracy_vectorized,
            test_labels=test_labels,
            k=k,
        )

    return Task2Results(
        task2_results=Results(
            predictions=predictions_vectorized,
            execution_time=time_vectorized,
            accuracy=accuracy_vectorized,
        ),
        task1_results=results_iterative,
        train_features=train_features,
        test_features=test_features,
        train_labels=train_labels,
        test_labels=test_labels,
        k=k,
    )

if __name__ == "__main__":
    task_2(show_results=True)
