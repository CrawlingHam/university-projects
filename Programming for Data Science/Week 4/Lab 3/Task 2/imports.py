from sys import path as sys_path
from os import path
import time

current_dir = path.dirname(path.abspath(__file__))
utils_path = path.join(current_dir, "..", "..", "..", "..", "utils")
sys_path.insert(0, utils_path)
from path import with_path  # pyright: ignore[reportMissingImports]
sys_path.remove(utils_path)

conversion = with_path(
    fn=lambda: __import__("importlib").import_module("src.utils.conversion").Conversion(),
    relative_path=("..", "..", "..", "..", "Introduction to Data Science", "project"),
    current_dir=current_dir,
)

load_module, evaluate_module = with_path(
    fn=lambda: (__import__("load"), __import__("evaluate")),
    relative_path=("..", "task 1"),
    current_dir=current_dir,
)

separate_features_and_labels = load_module.separate_features_and_labels
calculate_accuracy = evaluate_module.calculate_accuracy
from distance import distance_between_points
knn_predict = evaluate_module.knn_predict
load_dataset = load_module.load_dataset
from display import display_results