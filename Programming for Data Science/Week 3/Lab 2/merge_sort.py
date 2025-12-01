from random import randint


def merge_sort(array: list[int], recursion_count: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    
    recursion_count[0] += 1
    mid = len(array) // 2
    left = merge_sort(array[:mid], recursion_count)
    right = merge_sort(array[mid:], recursion_count)
    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    test_count = 10

    for i in range(test_count):
        array = [randint(1, 100) for _ in range(10)]
        print(f"Unsorted array: {array}")
        recursion_count = [0]
        sorted_array = merge_sort(array, recursion_count)
        print(f"Sorted array: {sorted_array}")
        print(f"Number of recursions: {recursion_count[0]}\n")
