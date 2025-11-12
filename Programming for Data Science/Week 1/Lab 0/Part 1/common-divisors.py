from random import randint

def find_common_divisors(a: int, b: int) -> list[int]:
    divisors = []

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
            
    return divisors

if __name__ == "__main__":
    a, b = [randint(1, 100) for _ in range(2)]
    print(f"The common divisors of {a} and {b} are: {find_common_divisors(a, b)}")