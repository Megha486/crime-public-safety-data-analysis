
"""
Create a simulated crime dataset for the project.

The dataset contains 240 original records, missing values
and deliberately introduced duplicate records.
"""

import numpy as np
import pandas as pd

from pathlib import Path


def create_crime_dataset():
    """
    Generate a simulated crime dataset.

    Returns:
        pandas.DataFrame: Dataset containing crime records.
    """

    # Fix the random seed to make the dataset reproducible.
    rng = np.random.default_rng(42)

    # Possible values for categorical attributes.
    states = [
        "Meghalaya",
        "Assam",
        "Tripura",
        "Manipur",
        "Mizoram"
    ]

    crime_types = [
        "Theft",
        "Robbery",
        "Assault",
        "Cybercrime",
        "Burglary"
    ]

    area_types = ["Urban", "Rural"]

    # Generate 240 records.
    number_of_records = 240

    data = {
        "Date": rng.choice(
            pd.date_range("2025-01-01", periods=365),
            size=number_of_records
        ),
        "State": rng.choice(states, size=number_of_records),
        "Crime_Type": rng.choice(
            crime_types, size=number_of_records
        ),
        "Area_Type": rng.choice(
            area_types, size=number_of_records
        ),
        "Victim_Age": rng.integers(
            18, 71, size=number_of_records
        ),
        "Reported_Cases": rng.integers(
            5, 31, size=number_of_records
        )
    }

    # Arrests cannot exceed reported cases.
    data["Arrests"] = [
        rng.integers(0, cases + 1)
        for cases in data["Reported_Cases"]
    ]

    # Convert the dictionary into a pandas DataFrame.
    df = pd.DataFrame(data)

    # Introduce missing values.
    df.loc[[3, 17, 41, 89, 130], "Victim_Age"] = np.nan
    df.loc[[8, 55, 110], "State"] = np.nan

    # Introduce duplicate records.
    duplicate_rows = df.iloc[[2, 8, 15, 30, 45, 60, 75, 90]]

    df = pd.concat(
        [df, duplicate_rows],
        ignore_index=True
    )

    return df


if __name__ == "__main__":

    # Generate the dataset.
    crime_data = create_crime_dataset()

    # Find the project root directory.
    project_root = Path(__file__).resolve().parent.parent.parent

    # Define the data folder.
    data_folder = project_root / "data"

    # Create the folder if it does not exist.
    data_folder.mkdir(parents=True, exist_ok=True)

    # Save the dataset as a CSV file.
    output_path = data_folder / "crime_data.csv"

    crime_data.to_csv(output_path, index=False)

    print("Crime dataset created successfully!")
    print("Total records:", len(crime_data))
    print("Total attributes:", len(crime_data.columns))
    print("Saved at:", output_path)
    print("\nFirst five records:")
    print(crime_data.head())
