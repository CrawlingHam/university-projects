def display_results(k: int, accuracy: float, predictions: list[str], test_labels: list[str], time_vectorized: float, time_iterative: float) -> None:
    print(f"\nIterative Implementation:  {time_iterative:.6f} seconds")
    print(f"Vectorized Implementation: {time_vectorized:.6f} seconds")
    speedup = time_iterative / time_vectorized if time_vectorized > 0 else 0
    print(f"Speedup: {speedup:.2f}x faster\n")
    
    print(f"KNN Algorithm Results (k={k}) - Vectorized Implementation:")
    print(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"\nTotal test points: {len(test_labels)}")
    print(f"Correct predictions: {sum(1 for p, a in zip(predictions, test_labels) if p == a)}")
    print(f"Incorrect predictions: {sum(1 for p, a in zip(predictions, test_labels) if p != a)}")

    print("\nSample predictions:")
    print("Prediction\tActual\t\tMatch")
    print("-" * 40)

    for i in range(min(10, len(predictions))):
        match = "✓" if predictions[i] == test_labels[i] else "✗"
        print(f"{predictions[i]:<15}\t{test_labels[i]:<15}\t{match}")
