from numpy import ndarray as np_ndarray
from dataclasses import dataclass
from pandas import DataFrame

@dataclass
class Results:
    predictions: list[int]
    execution_time: float
    accuracy: float

@dataclass
class Task2Results:
    train_features: list[list[float]]
    test_features: list[list[float]]
    train_labels: list[str]
    test_labels: list[str]
    task1_results: Results
    task2_results: Results
    k: int

@dataclass
class Task3Results:
    cluster_assignments: np_ndarray
    final_centroids: np_ndarray
    execution_time: float
    features: np_ndarray
    k: int

@dataclass
class KNNSklearnResults:
    predictions: list[int]
    execution_time: float
    accuracy: float

@dataclass
class KMeansSklearnResults:
    cluster_assignments: np_ndarray
    final_centroids: np_ndarray
    execution_time: float
    n_iter: int

@dataclass
class SeparateFeaturesAndLabelsResults:
    features: list[list[float]]
    labels: list[str]

@dataclass
class LoadDataframesResults:
    train_dataframe: DataFrame
    test_dataframe: DataFrame

@dataclass
class LoadDataframesAsListsResults:
    train_dataframe_list: list[list[float]]
    test_dataframe_list: list[list[float]]

@dataclass
class LoadAndSeparateDataframesAsListsResults:
    train_features: list[list[float]]
    test_features: list[list[float]]
    train_labels: list[str]
    test_labels: list[str]

@dataclass
class LoadAndSeparateDataframesAsArraysResults:
    features: np_ndarray
    labels: np_ndarray

@dataclass
class PrepareDataframesResults:
    train_features: list[list[float]]
    test_features: list[list[float]]
    train_labels: list[str]
    test_labels: list[str]
    k: int