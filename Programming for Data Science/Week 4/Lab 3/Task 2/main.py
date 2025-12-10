from imports import *

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

k = conversion.to_int(
    err_msg="Invalid input. Please enter a positive number.",
    prompt="Enter the number of neighbors: ", 
    additional_checks=lambda x: x > 0
)

print("\nRunning Iterative Implementation...")
start_time = time.time()
predictions_iterative = knn_predict(test_features, train_features, train_labels, k, distance_between_points)
accuracy_iterative = calculate_accuracy(predictions_iterative, test_labels)
end_time = time.time()
time_iterative = end_time - start_time

print("Running Vectorized Implementation...")
start_time = time.time()
predictions_vectorized = knn_predict(test_features, train_features, train_labels, k, distance_between_points)
accuracy_vectorized = calculate_accuracy(predictions_vectorized, test_labels)
end_time = time.time()
time_vectorized = end_time - start_time

display_results(
    predictions=predictions_vectorized,
    time_vectorized=time_vectorized,
    time_iterative=time_iterative,
    accuracy=accuracy_vectorized,
    test_labels=test_labels,
    k=k,
)
