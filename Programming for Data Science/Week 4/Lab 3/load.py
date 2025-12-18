from pandas import DataFrame, read_csv, concat as pd_concat
from numpy import array as np_array
from os import path
from data_types import (
    LoadAndSeparateDataframesAsArraysResults,
    LoadAndSeparateDataframesAsListsResults,
    SeparateFeaturesAndLabelsResults,
    LoadDataframesAsListsResults,
    LoadDataframesResults,
)

def load_dataset(file_path: str, clean: bool = False, columns: list[str] = None) -> DataFrame:
    dataframe: DataFrame = read_csv(file_path)

    if clean:
        dataframe.columns = dataframe.columns.str.strip().str.upper()
    if columns:
        columns = [col.strip().upper() for col in columns] if clean else columns
        dataframe = dataframe[columns]

    return dataframe

def separate_features_and_labels(data: list[list]) -> SeparateFeaturesAndLabelsResults:
    features: list[list[float]] = []
    labels: list[str] = []

    for row in data:
        features.append([float(x) for x in row[:-1]])
        labels.append(str(row[-1]))

    return SeparateFeaturesAndLabelsResults(features=features, labels=labels)

def load_dataframes() -> LoadDataframesResults:
    columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
    dataset_path = path.join(path.dirname(__file__), "iris_dataset")

    train_dataframe = load_dataset(
            file_path=path.join(dataset_path,"iris_train.csv"),
            columns=columns,
            clean=True, 
        )
    test_dataframe = load_dataset(
            file_path=path.join(dataset_path, "iris_test.csv"),
            columns=columns,
            clean=True,
        )

    return LoadDataframesResults(train_dataframe=train_dataframe, test_dataframe=test_dataframe)

def load_dataframes_as_lists() -> LoadDataframesAsListsResults:
    load_dataframes_results = load_dataframes()
    train_dataframe = load_dataframes_results.train_dataframe
    test_dataframe = load_dataframes_results.test_dataframe

    return LoadDataframesAsListsResults(
        train_dataframe_list=train_dataframe.values.tolist(),
        test_dataframe_list=test_dataframe.values.tolist(),
    )

def load_and_separate_dataframes_as_lists() -> LoadAndSeparateDataframesAsListsResults:
    load_dataframes_as_lists_results = load_dataframes_as_lists()
    train_dataframe_list = load_dataframes_as_lists_results.train_dataframe_list
    test_dataframe_list = load_dataframes_as_lists_results.test_dataframe_list

    train_separate_features_and_labels_results = separate_features_and_labels(train_dataframe_list)
    test_separate_features_and_labels_results = separate_features_and_labels(test_dataframe_list)

    return LoadAndSeparateDataframesAsListsResults(
        train_features=train_separate_features_and_labels_results.features,
        test_features=test_separate_features_and_labels_results.features,
        train_labels=train_separate_features_and_labels_results.labels,
        test_labels=test_separate_features_and_labels_results.labels,
    )

def load_and_separate_dataframes_as_arrays() -> LoadAndSeparateDataframesAsArraysResults:
    load_dataframes_results = load_dataframes()
    train_dataframe = load_dataframes_results.train_dataframe
    test_dataframe = load_dataframes_results.test_dataframe

    merged_dataframe = pd_concat([train_dataframe, test_dataframe], ignore_index=True)
    merged_dataframe_list = merged_dataframe.values.tolist()
    
    separate_features_and_labels_results = separate_features_and_labels(merged_dataframe_list)
    features = separate_features_and_labels_results.features
    labels = separate_features_and_labels_results.labels

    return LoadAndSeparateDataframesAsArraysResults(features=np_array(features), labels=np_array(labels))
    