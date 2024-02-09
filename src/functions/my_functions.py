import pandas as pd


def add_integers(x: int, y: int) -> int:
    return x + y


def subtract_column_integers(dataframe: pd.DataFrame, column1: str , column2: str) -> pd.DataFrame:
    dataframe["Subtracted"] = dataframe[column1] - dataframe[column2]
    return dataframe