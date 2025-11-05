from random import randint

def predict_next_polynomial_value(values: list[float]) -> float:
    differences: list[list[float]] = [values]
    found_constant = False
    
    #Get successive differences lists
    while len(differences[-1]) > 1:
        current = differences[-1]
        next_difference = [current[i+1] - current[i] for i in range(len(current)-1)]
        differences.append(next_difference)
        
        # Break if differences are constant or only one value is left
        if len(next_difference) > 1 and len(set(next_difference)) == 1:
            found_constant = True
            break
    
    # Only extrapolate if we found constant differences. Handle single value case
    constant_difference = differences[-1][0]
    if not found_constant:
        if len(differences[-1]) == 1:
            # Use the single value as the constant difference
            constant_difference = differences[-1][0]
        else:
            raise ValueError("Cannot extrapolate: sequence does not follow a polynomial pattern")

    # Calculate the next value starting with the constant difference
    next_value = constant_difference
    for prev in reversed(differences[:-1]):
        next_value = prev[-1] + next_value
    
    return next_value

if __name__ == "__main__":
    values = [randint(1, 100) for _ in range(10)]
    print(f"The next value predicted for the given values {values} is: {predict_next_polynomial_value(values)}")