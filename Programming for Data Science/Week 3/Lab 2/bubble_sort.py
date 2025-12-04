from random import randint

def bubble_sort(array: list[int]) -> int:
    array_len = len(array)
    comparisons = 0

    for i in range(array_len):
        for j in range(0, array_len - i - 1):
            comparisons += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return comparisons

if __name__ == "__main__":
    test_count = 10
    array_size = 10

    for i in range(test_count):
        array = [randint(1, 100) for _ in range(array_size)]
        print(f"Unsorted array: {array}")
        comparisons = bubble_sort(array)
        print(f"Sorted array: {array}")
        print(f"Number of pairwise comparisons: {comparisons}\n")
