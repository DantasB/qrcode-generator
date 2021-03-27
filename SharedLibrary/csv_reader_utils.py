import pandas as pd


def csv_to_dataframe(csv_path: str) -> pd.DataFrame:
    """ Convert csv to pandas dataframe

    Args:
        csv_path (str): path to the csv file

    Returns:
        DataFrame: the csv as dataframe
    """
    return pd.read_csv(csv_path)
