from data_models.models import BinarySearchResult, BinarySearchResults
from utils.display import display_binary_search_result
from random import randint

def binary_search(arr: list[int], low: int, high: int, x: int) -> BinarySearchResult:
    recursion_count = 0

    if high < low:
        return BinarySearchResult(
            recursion_count=recursion_count,
            all_indices=[],
            found=False,
            result=-1,
        )

    mid = low + (high - low) // 2

    if arr[mid] == x:
        return BinarySearchResult(
            recursion_count=recursion_count,
            all_indices=[],
            found=True,
            result=mid,
        )
    
    elif arr[mid] > x:
        binary_search_result = binary_search(arr, low, mid-1, x)
        recursion_count += 1
        return BinarySearchResult(
            recursion_count=recursion_count + binary_search_result.recursion_count,
            all_indices=binary_search_result.all_indices,
            result=binary_search_result.result,
            found=binary_search_result.found,
        )
    else:
        binary_search_result = binary_search(arr, mid + 1, high, x)
        recursion_count += 1
        return BinarySearchResult(
            recursion_count=recursion_count + binary_search_result.recursion_count,
            all_indices=binary_search_result.all_indices,
            result=binary_search_result.result,
            found=binary_search_result.found,
        )
 
if __name__ == "__main__":
    results: list[BinarySearchResults] = []
    duplicate_cell_count = 3
    test_count = 10
    array_size = 10
    
    for i in range(test_count):
        if i < duplicate_cell_count:
            array = [randint(1, 20) for _ in range(array_size)]
            sorted_array = sorted(array)
            target = sorted_array[randint(0, len(sorted_array) - 1)]
        else:
            array = [randint(1, 100) for _ in range(array_size)]
            sorted_array = sorted(array)
            target = randint(1, 100)
        
        binary_search_result = binary_search(sorted_array, 0, len(sorted_array) - 1, target)
        binary_search_result.all_indices = [i for i, val in enumerate(sorted_array) if val == target]

        results.append(BinarySearchResults(
            recursion_count=binary_search_result.recursion_count,
            all_indices=binary_search_result.all_indices,
            result=binary_search_result.result,
            found=binary_search_result.found,
            sorted_array=sorted_array,
            target=target,
        ))
    
    display_binary_search_result(results)