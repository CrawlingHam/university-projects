from data_models.models import ListType, PerformanceComparison, PlotData
from utils.display import displayPlots, displayTable
from utils.list import generate_list
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quicksort import quicksort
from time import perf_counter

def performance_comparison(array_size: int, trials: int, list_type: ListType = "random") -> PerformanceComparison:
    quicksort_recursions: list[int] = []
    bubble_comparisons: list[int] = []
    quicksort_times: list[float] = []
    merge_recursions: list[int] = []
    builtin_times: list[float] = []
    bubble_times: list[float] = []
    merge_times: list[float] = []
    
    for _ in range(trials):
        array = generate_list(list_type, array_size)
        
        arr_copy = array.copy()
        start = perf_counter()
        comparisons = bubble_sort(arr_copy)
        bubble_times.append(perf_counter() - start)
        bubble_comparisons.append(comparisons)
        
        arr_copy = array.copy()
        recursion_count = [0]
        start = perf_counter()
        merge_sort(arr_copy, recursion_count)
        merge_times.append(perf_counter() - start)
        merge_recursions.append(recursion_count[0])
        
        arr_copy = array.copy()
        recursion_count = [0]
        start = perf_counter()
        quicksort(arr_copy, recursion_count)
        quicksort_times.append(perf_counter() - start)
        quicksort_recursions.append(recursion_count[0])
        
        arr_copy = array.copy()
        start = perf_counter()
        sorted(arr_copy)
        builtin_times.append(perf_counter() - start)
    
    return PerformanceComparison(
        quicksort_recursions=sum(quicksort_recursions) / trials,
        bubble_comparisons=sum(bubble_comparisons) / trials,
        merge_recursions=sum(merge_recursions) / trials,
        quicksort_time=sum(quicksort_times) / trials,
        builtin_time=sum(builtin_times) / trials,
        bubble_time=sum(bubble_times) / trials,
        merge_time=sum(merge_times) / trials,
        list_type=list_type,
        size=array_size,
    )

if __name__ == "__main__":
    list_types: list[ListType] = ["sorted", "almost_sorted", "random", "reverse_sorted"]
    labels: list[str] = ["Built-in sorted()", "Bubble Sort", "Merge Sort", "Quicksort"]
    all_results: dict[ListType, list[PerformanceComparison]] = {}
    markers: list[str] = ["o", "s", "^", "D"]
    all_plot_data: list[PlotData] = []
    sizes: list[int] = [10, 100, 1000]
    y_label = "Time (seconds)"
    x_label = "Array Size"
    trials = 10
    
    for list_type in list_types:
        results: list[PerformanceComparison] = []
        
        for size in sizes:
            results.append(performance_comparison(size, trials, list_type))
        
        all_results[list_type] = results

    for list_type in list_types:
        results = all_results[list_type]
        displayTable(results, list_type)
        
        quicksort_times = [r.quicksort_time for r in results]
        builtin_times = [r.builtin_time for r in results]
        bubble_times = [r.bubble_time for r in results]
        merge_times = [r.merge_time for r in results]
        sizes_list = [r.size for r in results]
        
        title = f"Sorting Algorithm Performance - {list_type.upper().replace('_', ' ')}"
        data = [builtin_times, bubble_times, merge_times, quicksort_times]
        
        all_plot_data.append(PlotData(
            sizes=sizes_list,
            x_label=x_label,
            y_label=y_label,
            title=title,
            data=data,
        ))
    
    displayPlots(data=all_plot_data, labels=labels, markers=markers)
