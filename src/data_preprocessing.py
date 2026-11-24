
"""
Data preprocessing module for the Crime and Public Safety
Data Analysis System.

This module identifies missing values, removes duplicate
records, corrects data types and saves cleaned data.
"""

from pathlib import Path

import pandas as pd

from data_loader import load_dataset


def preprocess_data(df):
    """
    Clean a dataset by handling missing values, duplicates
    and inconsistent data types.

    Parameters:
        df (pandas.DataFrame): Original dataset.

    Returns:
        pandas.DataFrame: Cleaned dataset.
    """

    # Work on a copy so the original data remains unchanged.
    df = df.copy()

    print("\nStarting data preprocessing...")

    # Step 1: Display missing values before cleaning.
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    # Step 2: Remove duplicate records.
    original_count = len(df)

    df = df.drop_duplicates().copy()

    duplicates_removed = original_count - len(df)

    print("\nDuplicate records removed:", duplicates_removed)

    # Step 3: Correct numerical data types.
    numeric_columns = [
        "Victim_Age",
        "Reported_Cases",
        "Arrests"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column], errors="coerce"
            )

    # Step 4: Convert the Date column into datetime format.
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"], errors="coerce"
        )

    # Step 5: Handle missing values.
    for column in df.columns:

        if df[column].isnull().sum() > 0:

            # Fill numerical missing values with the median.
            if pd.api.types.is_numeric_dtype(df[column]):

                median_value = df[column].median()

                if pd.notna(median_value):
                    df[column] = df[column].fillna(median_value)

            # Fill date or categorical missing values with the mode.
            else:
                mode_values = df[column].mode()

                if not mode_values.empty:
                    df[column] = df[column].fillna(
                        mode_values.iloc[0]
                    )

    # Step 6: Display missing values after cleaning.
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    print("\nPreprocessing completed successfully!")

    return df


def main():
    """
    Load, preprocess and save the crime dataset.
    """

    # Locate the main project directory.
    project_root = Path(__file__).resolve().parent.parent

    # Locate the original dataset.
    input_path = project_root / "data" / "crime_data.csv"

    # Locate the output directory.
    output_folder = project_root / "output"

    # Create output directory if it does not exist.
    output_folder.mkdir(parents=True, exist_ok=True)

    # Load the original dataset.
    original_data = load_dataset(input_path)

    # Clean the dataset.
    cleaned_data = preprocess_data(original_data)

    # Save the cleaned dataset.
    output_path = output_folder / "cleaned_crime_data.csv"

    cleaned_data.to_csv(output_path, index=False)

    print("\nOriginal records:", len(original_data))
    print("Cleaned records:", len(cleaned_data))
    print("Total attributes:", len(cleaned_data.columns))
    print("Cleaned dataset saved at:", output_path)


if __name__ == "__main__":
    main()
