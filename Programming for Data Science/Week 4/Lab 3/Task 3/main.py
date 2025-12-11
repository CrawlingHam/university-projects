from display import display_results
from kmeans import kmeans
from imports import *

dataset_path = path.join(path.dirname(__file__), "..", "iris_dataset")

train_dataframe = load_dataset(
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"],
    file_path=path.join(dataset_path, "iris_train.csv"),
    clean=True,
)

test_dataframe = load_dataset(
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"],
    file_path=path.join(dataset_path, "iris_test.csv"),
    clean=True,
)

merged_dataframe = pd_concat([train_dataframe, test_dataframe], ignore_index=True)
merged_dataframe_list = merged_dataframe.values.tolist()
features, _ = separate_features_and_labels(merged_dataframe_list)

data = np_array(features)

k = conversion.to_int(
    err_msg="Invalid input. Please enter a positive number.",
    prompt="Enter the number of clusters (k): ",
    additional_checks=lambda x: x > 0
)

start_time = time_time()
cluster_assignments, final_centroids = kmeans(data, k)
end_time = time_time()
execution_time = end_time - start_time

display_results(data, execution_time, k, cluster_assignments, final_centroids)
