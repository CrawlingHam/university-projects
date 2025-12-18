from sklearn.neighbors import KNeighborsClassifier
from time import perf_counter as time_perf_counter
from sklearn.metrics import accuracy_score
from data_types import KNNSklearnResults
from numpy import ndarray as np_ndarray

def knn_scikit_learn(
    train_features_array: np_ndarray,
    test_features_array: np_ndarray,
    train_labels: list[str],
    test_labels: list[str],
    k: int
) -> KNNSklearnResults:
    start_time = time_perf_counter()
    
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_features_array, train_labels)

    predictions = knn.predict(test_features_array)
    accuracy = accuracy_score(test_labels, predictions)

    knn_time = time_perf_counter() - start_time
    
    return KNNSklearnResults(
        predictions=predictions.tolist(),
        execution_time=knn_time,
        accuracy=accuracy,
    )