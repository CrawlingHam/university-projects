from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from pandas import read_csv
from os import path

# Check for dataset in the same directory as the script
script_dir = path.dirname(path.abspath(__file__))
iris_path = path.join(script_dir, "iris.csv")

df = read_csv(iris_path)
features = df.drop("class", axis=1)
classes = df["class"]

test_size = 0.4
random_state = 42
n_neighbors = 1

features_train, features_test, classes_train, classes_test = train_test_split(features, classes, test_size=test_size, random_state=random_state, stratify=classes)

knn = KNeighborsClassifier(n_neighbors)

knn.fit(features_train, classes_train)
predictions = knn.predict(features_test)

print(f"Predictions: {predictions}\n")
print(f"Accuracy: {accuracy_score(classes_test, predictions)}\n")

print(f"Classification Report:\n{classification_report(classes_test, predictions)}")