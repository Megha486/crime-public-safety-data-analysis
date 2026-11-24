
"""
Data analysis module for the Crime and Public Safety
Data Analysis System.

This module calculates descriptive statistics and
frequency distributions using NumPy and pandas.
"""

from pathlib import Path

import numpy as np
import pandas as pd

from data_loader import load_dataset


def analyze_data(df):
    """
    Calculate statistical summaries and frequency distributions.

    Parameters:
        df (pandas.DataFrame): Cleaned crime dataset.

    Returns:
        tuple:
            - pandas.DataFrame containing numerical statistics.
            - dictionary containing categorical frequencies.
    """

    # Identify all numerical columns.
    numeric_columns = df.select_dtypes(
        include=[np.number]
    ).columns

    # Store statistical results.
    statistics = []

    # Calculate statistics for every numerical column.
    for column in numeric_columns:

        values = df[column].dropna().to_numpy()

        if len(values) == 0:
            continue

        statistics.append({
            "Attribute": column,
            "Mean": np.mean(values),
            "Median": np.median(values),
            "Standard Deviation": (
                np.std(values, ddof=1)
                if len(values) > 1 else 0
            ),
            "Minimum": np.min(values),
            "Maximum": np.max(values)
        })

    # Convert statistical results into a DataFrame.
    statistics_df = pd.DataFrame(statistics)

    # Identify categorical columns.
    
    categorical_columns = df.select_dtypes(
    include=["object", "category", "str"]
)   .columns
    
    # Store frequency distributions.
    frequency_distributions = {}

    for column in categorical_columns:

        # Date values are better analysed as time trends.
        if "date" in column.lower():
            continue

        frequency_distributions[column] = (
            df[column].value_counts()
        )

    return statistics_df, frequency_distributions


def save_analysis_results(statistics_df, frequencies, output_folder):
    """
    Save statistical summaries and frequency distributions.

    Parameters:
        statistics_df (pandas.DataFrame): Statistical results.
        frequencies (dict): Categorical frequency results.
        output_folder (Path): Destination folder.

    Returns:
        None
    """

    output_folder.mkdir(parents=True, exist_ok=True)

    # Save numerical statistics.
    statistics_path = output_folder / "statistical_summary.csv"

    statistics_df.to_csv(statistics_path, index=False)

    print("\nStatistical summary saved at:", statistics_path)

    # Save frequency distributions separately.
    for column, frequency_data in frequencies.items():

        safe_column_name = (
            column.replace(" ", "_").lower()
        )

        frequency_path = (
            output_folder /
            f"frequency_{safe_column_name}.csv"
        )

        frequency_data.to_csv(
            frequency_path,
            header=["Frequency"]
        )

        print(
            f"Frequency distribution saved: {frequency_path}"
        )


def main():
    """
    Load cleaned data, perform statistical analysis
    and save the analysis results.
    """

    # Locate the project directory.
    project_root = Path(__file__).resolve().parent.parent

    # Locate the cleaned dataset.
    input_path = (
        project_root /
        "output" /
        "cleaned_crime_data.csv"
    )

    # Locate the output directory.
    output_folder = project_root / "output"

    # Load the cleaned dataset.
    crime_data = load_dataset(input_path)

    print("Dataset loaded for statistical analysis.")

    # Perform statistical analysis.
    statistics_df, frequencies = analyze_data(crime_data)

    # Display numerical statistics.
    print("\n========== STATISTICAL SUMMARY ==========")

    print(statistics_df.round(2).to_string(index=False))

    # Display categorical frequency distributions.
    print("\n========== FREQUENCY DISTRIBUTIONS ==========")

    for column, frequency_data in frequencies.items():

        print(f"\n{column}:")

        print(frequency_data.to_string())

    # Save all results.
    save_analysis_results(
        statistics_df,
        frequencies,
        output_folder
    )

    print("\nData analysis completed successfully!")


if __name__ == "__main__":
    main()
