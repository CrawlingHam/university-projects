from dataclasses import dataclass
from typing import Literal

type ListType = Literal["sorted", "reverse_sorted", "almost_sorted", "random"]

@dataclass
class PerformanceComparison:
    quicksort_recursions: int
    bubble_comparisons: int
    quicksort_time: float
    merge_recursions: int
    builtin_time: float
    list_type: ListType
    bubble_time: float
    merge_time: float
    size: int

@dataclass
class PlotData:
    data: list[list[float]]
    sizes: list[int]
    x_label: str
    y_label: str
    title: str

@dataclass
class BinarySearchResult:
    all_indices: list[int]
    recursion_count: int
    result: int
    found: bool

@dataclass
class BinarySearchResults:
    sorted_array: list[int]
    all_indices: list[int]
    recursion_count: int
    target: int
    result: int
    found: bool

@dataclass
class TreeSearchResult:
    bfs_visited_nodes: list[int]
    dfs_visited_nodes: list[int]