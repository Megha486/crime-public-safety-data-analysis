
"""
Data loading module for the Crime and Public Safety
Data Analysis System.

This module reads datasets from CSV and JSON files.
"""

from pathlib import Path

import pandas as pd


def load_dataset(file_path):
    """
    Load a dataset from a CSV or JSON file.

    Parameters:
        file_path (str or Path): Location of the input dataset.

    Returns:
        pandas.DataFrame: The loaded dataset.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the format is unsupported or the file is invalid.
    """

    # Convert the given path into a Path object.
    file_path = Path(file_path)

    # Check whether the file exists.
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    # Identify the file extension.
    file_extension = file_path.suffix.lower()

    try:

        # Read CSV files.
        if file_extension == ".csv":
            df = pd.read_csv(file_path)

        # Read JSON files.
        elif file_extension == ".json":
            df = pd.read_json(file_path)

        # Reject unsupported formats.
        else:
            raise ValueError(
                "Unsupported file format. Use CSV or JSON."
            )

    except pd.errors.EmptyDataError as error:
        raise ValueError("The CSV file is empty.") from error

    except ValueError as error:
        raise ValueError(
            f"Unable to read the dataset: {error}"
        ) from error

    # Check whether the dataset contains records.
    if df.empty:
        raise ValueError("The dataset contains no records.")

    return df


if __name__ == "__main__":

    # Locate the main project directory.
    project_root = Path(__file__).resolve().parent.parent

    # Locate our generated crime dataset.
    dataset_path = project_root / "data" / "crime_data.csv"

    # Load the dataset.
    crime_data = load_dataset(dataset_path)

    # Display the loaded dataset.
    print("Dataset loaded successfully!")
    print("Number of records:", len(crime_data))
    print("Number of attributes:", len(crime_data.columns))

    print("\nDataset preview:")
    print(crime_data.head())
