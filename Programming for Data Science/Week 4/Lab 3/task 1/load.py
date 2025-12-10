from pandas import DataFrame, read_csv

def load_dataset(file_path: str, clean: bool = False, columns: list[str] = None):
    dataframe: DataFrame = read_csv(file_path)

    if clean:
        dataframe.columns = dataframe.columns.str.strip().str.upper()
    if columns:
        columns = [col.strip().upper() for col in columns] if clean else columns
        dataframe = dataframe[columns]

    return dataframe

def separate_features_and_labels(data: list[list]) -> tuple[list[list[float]], list[str]]:
    features: list[list[float]] = []
    labels: list[str] = []

    for row in data:
        features.append([float(x) for x in row[:-1]])
        labels.append(str(row[-1]))
    return features, labels
