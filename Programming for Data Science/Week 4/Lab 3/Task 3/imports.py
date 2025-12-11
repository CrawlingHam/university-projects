from numpy import (
    ndarray as np_ndarray, zeros as np_zeros, mean as np_mean, 
    newaxis as np_newaxis, argmin as np_argmin, sum as np_sum,
    unique as np_unique, linalg as np_linalg, max as np_max,
    random as np_random, array as np_array,
)
from pandas import concat as pd_concat
from time import time as time_time
from sys import path as sys_path
from typing import Tuple
from os import path

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

load_module = with_path(
    fn=lambda: __import__("load"),
    relative_path=("..", "task 1"),
    current_dir=current_dir,
)

separate_features_and_labels = load_module.separate_features_and_labels
load_dataset = load_module.load_dataset
