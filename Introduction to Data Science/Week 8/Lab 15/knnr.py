from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from pandas import read_csv
from numpy import sqrt
from os import path

# Check for dataset in the same directory as the script
script_dir = path.dirname(path.abspath(__file__))
insurance_path = path.join(script_dir, "insurance.csv")

dataframe = read_csv(insurance_path)

features = dataframe.drop("charges", axis=1)
targets = dataframe["charges"]

n_neighbors: int = 1
random_state: int = 42
test_size: float = 0.2

features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=test_size, random_state=random_state)

knnr = KNeighborsRegressor(n_neighbors=n_neighbors)
knnr.fit(features_train, targets_train)

predictions = knnr.predict(features_test)

mae = mean_absolute_error(targets_test, predictions)
mse = mean_squared_error(targets_test, predictions)
rmse = sqrt(mse)

print(f"MAE: {mae:.3f}")
print(f"MSE: {mse:.3f}")
print(f"RMSE: {rmse:.3f}")
