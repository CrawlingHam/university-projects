from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from pandas import read_csv
from numpy import sqrt
from os import path

# Check for dataset in the same directory as the script
script_dir = path.dirname(path.abspath(__file__))
insurance_path = path.join(script_dir, "insurance.csv")

dataframe = read_csv(insurance_path)

categorical_features = ["sex", "smoker", "region"]
numerical_features = ["age", "bmi", "children"]

features = dataframe.drop("charges", axis=1)
targets = dataframe["charges"]

n_neighbors: int = 30
random_state: int = 42
test_size: float = 0.2

features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=test_size, random_state=random_state)

transformers = [
    ("cat", OneHotEncoder(), categorical_features),
    ("num", MinMaxScaler(), numerical_features)
]

preprocessor = ColumnTransformer(transformers=transformers)
preprocessor_features_train = preprocessor.fit_transform(features_train)
preprocessor_features_test = preprocessor.transform(features_test)

knnr = KNeighborsRegressor(n_neighbors=n_neighbors)
knnr.fit(preprocessor_features_train, targets_train)

predictions = knnr.predict(preprocessor_features_test)

mae = mean_absolute_error(targets_test, predictions)
mse = mean_squared_error(targets_test, predictions)
rmse = sqrt(mse)

print(f"MAE: {mae:.3f}")
print(f"MSE: {mse:.3f}")
print(f"RMSE: {rmse:.3f}")
