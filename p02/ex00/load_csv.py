import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load data from the path passed, check for the file format,
print the dataset shape and return the dataset."""
    try:
        data = pd.read_csv(path)
        assert path.endswith(".csv"), "file is not in .csv format"
        print("Loading dataset of dimensions", data.shape)
        return data
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except FileNotFoundError:
        print("FileNotFoundError: No such file or directory:", path)
    except pd.errors.EmptyDataError:
        print("pandas.errors.EmptyDataError: No columns to parse from file")
