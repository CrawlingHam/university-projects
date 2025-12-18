from task_4_kmeans import kmeans_scikit_learn
from task_4_display import display_results
from task_4_knn import knn_scikit_learn
from numpy import array as np_array
from task_3 import task_3
from task_2 import task_2

def task_4() -> None:
    knn_task_results = task_2()
    knn_vectorized_results = knn_task_results.task2_results
    knn_iterative_results = knn_task_results.task1_results

    knn_scikit_learn_results = knn_scikit_learn(
        train_features_array=np_array(knn_task_results.train_features),
        test_features_array=np_array(knn_task_results.test_features),
        train_labels=knn_task_results.train_labels,
        test_labels=knn_task_results.test_labels,
        k=knn_task_results.k,
    )

    kmeans_task_results = task_3()
    kmeans_scikit_learn_results = kmeans_scikit_learn(
        data=kmeans_task_results.features,
        k=kmeans_task_results.k,
    )

    display_results(
        kmeans_scikit_learn_results=kmeans_scikit_learn_results,
        knn_scikit_learn_results=knn_scikit_learn_results,
        knn_vectorized_results=knn_vectorized_results,
        knn_iterative_results=knn_iterative_results,
        kmeans_task_results=kmeans_task_results,
    )

if __name__ == "__main__":
    task_4()
