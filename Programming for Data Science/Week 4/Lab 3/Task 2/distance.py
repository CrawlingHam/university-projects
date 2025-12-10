from numpy import sqrt as np_sqrt, sum as np_sum, array as np_array

def distance_between_points(test_point: list[float], training_points: list[list[float]]) -> list[float]:
    training_points_array = np_array(training_points)
    test_point_array = np_array(test_point)
    
    squared_differences = (training_points_array - test_point_array) ** 2
    sum_of_squares = np_sum(squared_differences, axis=1)
    distances = np_sqrt(sum_of_squares)
    
    return distances.tolist()

