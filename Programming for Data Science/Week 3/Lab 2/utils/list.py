from data_models.models import ListType
from random import randint

def generate_list(list_type: ListType, array_size: int) -> list[int]:
    if list_type == "sorted":
        return list(range(1, array_size + 1))
    elif list_type == "reverse_sorted":
        return list(range(array_size, 0, -1))
    elif list_type == "almost_sorted":
        arr = list(range(1, array_size + 1))
        for _ in range(array_size // 10):
            i = randint(0, array_size - 1)
            j = randint(0, array_size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    else:
        return [randint(1, 1000) for _ in range(array_size)]