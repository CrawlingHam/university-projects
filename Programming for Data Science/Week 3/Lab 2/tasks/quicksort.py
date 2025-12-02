from random import randint


def quicksort(array: list[int], recursion_count: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    
    recursion_count[0] += 1
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    
    return quicksort(left, recursion_count) + middle + quicksort(right, recursion_count)


if __name__ == "__main__":
    test_count = 10
    array_size = 10

    for i in range(test_count):
        array = [randint(1, 100) for _ in range(array_size)]
        print(f"Unsorted array: {array}")
        recursion_count = [0]
        sorted_array = quicksort(array, recursion_count)
        print(f"Sorted array: {sorted_array}")
        print(f"Number of recursions: {recursion_count[0]}\n")
