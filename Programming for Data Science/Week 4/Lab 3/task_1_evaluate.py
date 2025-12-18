from collections import Counter
from typing import Callable

def find_k_nearest_neighbors(distances: list[float], k: int) -> list[int]:
    indexed_distances: list[tuple[float, int]] = [(dist, idx) for idx, dist in enumerate(distances)]
    indexed_distances.sort(key=lambda x: x[0])
    return [idx for _, idx in indexed_distances[:k]]

def majority_vote(labels: list[str]) -> str:
    counter: Counter[str] = Counter(labels)
    return counter.most_common(1)[0][0]

def knn_predict(test_features: list[list[float]], train_features: list[list[float]], train_labels: list[str], k: int, distance_function: Callable[[list[float], list[list[float]]], float]) -> list[str]:
    predictions: list[str] = []
    
    for test_point in test_features:
        distances: list[float] = distance_function(test_point, train_features)
        nearest_indices: list[int] = find_k_nearest_neighbors(distances, k)
        
        nearest_labels: list[str] = [train_labels[idx] for idx in nearest_indices]
        prediction: str = majority_vote(nearest_labels)
        predictions.append(prediction)
    
    return predictions

def calculate_accuracy(predictions: list[str], test_labels: list[str]) -> float:
    correct: int = sum(1 for pred, actual in zip(predictions, test_labels) if pred == actual)
    return correct / len(test_labels) if len(test_labels) > 0 else 0.0