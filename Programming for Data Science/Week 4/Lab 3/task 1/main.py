from load import load_dataset, separate_features_and_labels
from evaluate import knn_predict, calculate_accuracy
from distance import distance_between_points
from display import display_results
from sys import path as sys_path
from os import path

dataset_path = path.join(path.dirname(__file__), "..", "iris_dataset")

train_dataframe = load_dataset(
        file_path=path.join(dataset_path,"iris_train.csv"),
        clean=True, columns=["sepal_length", "sepal_width",
        "petal_length", "petal_width", "class"],
    )
test_dataframe = load_dataset(
        columns=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"],
        file_path=path.join(dataset_path, "iris_test.csv"),
        clean=True,
    )

train_dataframe_list = train_dataframe.values.tolist()
test_dataframe_list = test_dataframe.values.tolist()

train_features, train_labels = separate_features_and_labels(train_dataframe_list)
test_features, test_labels = separate_features_and_labels(test_dataframe_list)

# Get K from user
current_dir = path.dirname(path.abspath(__file__))
university_root = path.abspath(path.join(current_dir, "..", "..", "..", ".."))
project_dir = path.join(university_root, "Introduction to Data Science", "project")
sys_path.insert(0, path.abspath(project_dir))

from src.utils.conversion import Conversion  # pyright: ignore[reportMissingImports]

conversion = Conversion()

k = conversion.to_int(
    err_msg="Invalid input. Please enter a positive number.",
    prompt="Enter the number of neighbors: ", 
    additional_checks=lambda x: x > 0
)

# Predictions, accuracy and results
predictions = knn_predict(test_features, train_features, train_labels, k, distance_between_points)
accuracy = calculate_accuracy(predictions, test_labels)

display_results(k, accuracy, predictions, test_labels)
