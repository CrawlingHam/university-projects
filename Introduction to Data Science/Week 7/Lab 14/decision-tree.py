from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.tree import DecisionTreeClassifier
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
decision_tree_random_state = 77
n_neighbors = 1

features_train, features_test, classes_train, classes_test = train_test_split(features, classes, test_size=test_size, random_state=random_state, stratify=classes)

knn = KNeighborsClassifier(n_neighbors)
knn.fit(features_train, classes_train)
knn_predictions = knn.predict(features_test)

decision_tree = DecisionTreeClassifier(random_state=decision_tree_random_state)
decision_tree.fit(features_train, classes_train)
decision_tree_predictions = decision_tree.predict(features_test)

print(f"KNN Predictions: {knn_predictions}\n")
print(f"Accuracy: {accuracy_score(classes_test, knn_predictions)}\n")
print(f"Classification Report:\n{classification_report(classes_test, knn_predictions)}")
print("------------------------------------------------------------------------------\n\n")

print(f"Decision Tree Predictions: {decision_tree_predictions}\n")
print(f"Accuracy: {accuracy_score(classes_test, decision_tree_predictions)}\n")
print(f"Classification Report:\n{classification_report(classes_test, decision_tree_predictions)}")
