def display_results(k: int, accuracy: float, predictions: list[str], test_labels: list[str]) -> None:
    print(f"KNN Algorithm Results (k={k}):")
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