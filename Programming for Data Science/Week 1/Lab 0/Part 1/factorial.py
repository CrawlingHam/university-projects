from random import randint
from math import prod

def get_factorial(number: int) -> int:
    return prod([i for i in range(1, number + 1)])

def get_factorial_with_loop(number: int) -> int:
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

if __name__ == "__main__":
    test_number = randint(1, 100)
    print(get_factorial(test_number))
    print(get_factorial_with_loop(test_number))
