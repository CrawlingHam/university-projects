from random import randint

def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

if __name__ == "__main__":
    test_number = randint(1, 100)
    print(is_prime(test_number))