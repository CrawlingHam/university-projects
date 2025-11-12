from factorial import get_factorial
from random import randint

def binomial_coefficient(n: int, k: int) -> int:
    return get_factorial(n) // (get_factorial(k) * get_factorial(n - k))

def khayyam_pascal_triangle(rows: int) -> list[list[int]]:
    triangle: list[list[int]] = []
    
    for n in range(rows):
        row: list[int] = []
        for k in range(n + 1):
            row.append(binomial_coefficient(n, k))
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    rows = randint(1, 10)
    triangle = khayyam_pascal_triangle(rows)

    for row in triangle:
        print(row)