from task_1_evaluate import knn_predict, calculate_accuracy
from data_types import Results, PrepareDataframesResults
from load import load_and_separate_dataframes_as_lists
from task_1_distance import distance_between_points
from time import perf_counter as time_perf_counter
from task_1_display import display_results

def prepare_dataframes() -> PrepareDataframesResults:
    load_and_separate_dataframes_as_lists_results = load_and_separate_dataframes_as_lists()
    train_features = load_and_separate_dataframes_as_lists_results.train_features
    test_features = load_and_separate_dataframes_as_lists_results.test_features
    train_labels = load_and_separate_dataframes_as_lists_results.train_labels
    test_labels = load_and_separate_dataframes_as_lists_results.test_labels

    k = int(input("Enter the number of neighbors: "))
    return PrepareDataframesResults(
        train_features=train_features,
        test_features=test_features,
        train_labels=train_labels,
        test_labels=test_labels,
        k=k,
    )

def task_1(
        train_features: list[list[float]] = None,
        test_features: list[list[float]] = None,
        train_labels: list[str] = None,
        test_labels: list[str] = None,
        show_results: bool = False,
        k: int = None,
    ) -> Results:
    if train_features is None or train_labels is None or test_features is None or test_labels is None or k is None:
        prepare_dataframes_results = prepare_dataframes()
        train_features = prepare_dataframes_results.train_features
        test_features = prepare_dataframes_results.test_features
        train_labels = prepare_dataframes_results.train_labels
        test_labels = prepare_dataframes_results.test_labels
        k = prepare_dataframes_results.k

    start_time = time_perf_counter()
    predictions = knn_predict(
        distance_function=distance_between_points,
        train_features=train_features,
        test_features=test_features,
        train_labels=train_labels,
        k=k,
    )
    end_time = time_perf_counter()
    execution_time = end_time - start_time
    
    accuracy = calculate_accuracy(predictions=predictions, test_labels=test_labels)

    if show_results:
        display_results(k, accuracy, predictions, test_labels, execution_time)

    return Results(
        execution_time=execution_time,
        predictions=predictions,
        accuracy=accuracy,
    )

if __name__ == "__main__":
    task_1(show_results=True)