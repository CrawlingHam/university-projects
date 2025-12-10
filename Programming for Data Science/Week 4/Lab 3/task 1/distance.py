from math import sqrt

def euclidean_distance(point1: list[float], point2: list[float]) -> float:
    sum_of_squares = sum((a - b) ** 2 for a, b in zip(point1, point2))
    return sqrt(sum_of_squares)

def distance_between_points(test_point: list[float], training_points: list[list[float]]) -> list[float]:
    distances: list[float] = []
    for train_point in training_points:
        distance = euclidean_distance(test_point, train_point)
        distances.append(distance)
    return distances
