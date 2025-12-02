from data_models.models import PlotData, PerformanceComparison, ListType, BinarySearchResults
import matplotlib.pyplot as plt

def displayPlot(sizes: list[int], title: str, x_label: str, y_label: str, data: list[list[float]], labels: list[str], markers: list[str]) -> None:
    plt.figure(figsize=(10, 6))

    for i in range(len(data)):
        plt.plot(sizes, data[i], marker=markers[i], label=f'{labels[i]}')

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

def displayPlots(data: list[PlotData], labels: list[str], markers: list[str]) -> None:
    _fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    axes = axes.flatten()
    
    for idx, plot_data in enumerate(data):
        ax = axes[idx]
        for i in range(len(plot_data.data)):
            ax.plot(plot_data.sizes, plot_data.data[i], marker=markers[i], label=labels[i])
        
        ax.set_xlabel(plot_data.x_label)
        ax.set_ylabel(plot_data.y_label)
        ax.set_title(plot_data.title)
        ax.grid(True)
        ax.legend()
    
    plt.tight_layout()
    plt.show()

def displayTable(results: list[PerformanceComparison], list_type: ListType) -> None:
    print(f"\n{'='*150}")
    print(f"List Type: {list_type.upper().replace('_', ' ')}")
    print(f"{'='*150}")
    print(f"{'Size':<10} {'Bubble Time (s)':<18} {'Bubble Comparisons':<20} {'Merge Time (s)':<18} {'Merge Recursions':<20} {'Quick Time (s)':<18} {'Quick Recursions':<20} {'Built-in Time (s)':<18}")
    print("-" * 150)
    for r in results:
        print(f"{r.size:<10} {r.bubble_time:<18.6f} {r.bubble_comparisons:<20.1f} {r.merge_time:<18.6f} {r.merge_recursions:<20.1f} {r.quicksort_time:<18.6f} {r.quicksort_recursions:<20.1f} {r.builtin_time:<18.6f}")

def display_binary_search_result(results: list[BinarySearchResults]) -> None:
    print(f"\n{'='*140}")
    print(f"{'Test':<6} {'Array':<35} {'Target':<8} {'Found':<8} {'Index':<8} {'Recursions':<12} {'All Indices':<20} {'Has Duplicates':<15}")
    print("-" * 140)
    for idx, result in enumerate(results, 1):
        array_str = str(result.sorted_array)[:33] + "..." if len(str(result.sorted_array)) > 35 else str(result.sorted_array)
        found_str = "Yes" if result.found else "No"
        index_str = str(result.result) if result.found else "N/A"
        all_indices_str = str(result.all_indices) if result.found else "N/A"
        has_duplicates = "Yes" if result.found and len(result.all_indices) > 1 else "No"
        print(f"{idx:<6} {array_str:<35} {result.target:<8} {found_str:<8} {index_str:<8} {result.recursion_count:<12} {all_indices_str:<20} {has_duplicates:<15}")
    print("=" * 140)