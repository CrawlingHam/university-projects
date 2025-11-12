from random import randint

def sqrt_newton(n: float, precision: float = 1e-10) -> float:
    """Approximates the square root of a natural number using Newton's method."""
    
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if n == 0:
        return 0

    x = n / 2 # First guess

    while abs(x * x - n) > precision:
        x = 0.5 * (x + n / x)

    return x

if __name__ == "__main__":
    test_number = randint(1, 100)
    print(sqrt_newton(test_number))