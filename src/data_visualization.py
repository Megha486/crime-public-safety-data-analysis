
"""
Data visualization module for the Crime and Public
Safety Data Analysis System.

This module creates three visualizations using Matplotlib:
1. Crime type distribution.
2. Victim age distribution.
3. Monthly reported crime trend.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from data_loader import load_dataset


def create_crime_type_chart(df, output_folder):
    """
    Create a bar chart showing crime type distribution.

    Parameters:
        df: Cleaned crime dataset.
        output_folder: Folder where the chart will be saved.

    Returns:
        None
    """

    # Count the occurrences of each crime type.
    crime_counts = df["Crime_Type"].value_counts()

    # Create the figure.
    plt.figure(figsize=(10, 6))

    # Create the bar chart.
    plt.bar(
        crime_counts.index,
        crime_counts.values
    )

    # Add chart details.
    plt.title("Distribution of Crime Types")
    plt.xlabel("Crime Type")
    plt.ylabel("Number of Records")
    plt.xticks(rotation=45)

    plt.tight_layout()

    # Save the chart.
    plt.savefig(
        output_folder / "crime_type_distribution.png",
        dpi=300
    )

    plt.close()

    print("Crime type chart saved successfully.")


def create_victim_age_histogram(df, output_folder):
    """
    Create a histogram showing the distribution of victim ages.

    Parameters:
        df: Cleaned crime dataset.
        output_folder: Folder where the chart will be saved.

    Returns:
        None
    """

    # Remove missing age values.
    ages = df["Victim_Age"].dropna()

    # Create the figure.
    plt.figure(figsize=(10, 6))

    # Create the histogram.
    plt.hist(
        ages,
        bins=10,
        edgecolor="black"
    )

    # Add chart details.
    plt.title("Distribution of Victim Ages")
    plt.xlabel("Victim Age")
    plt.ylabel("Frequency")

    plt.tight_layout()

    # Save the chart.
    plt.savefig(
        output_folder / "victim_age_distribution.png",
        dpi=300
    )

    plt.close()

    print("Victim age histogram saved successfully.")


def create_monthly_crime_chart(df, output_folder):
    """
    Create a line chart showing monthly reported crime cases.

    Parameters:
        df: Cleaned crime dataset.
        output_folder: Folder where the chart will be saved.

    Returns:
        None
    """

    # Convert the Date column into datetime format.
    data = df.copy()

    data["Date"] = pd.to_datetime(
        data["Date"],
        errors="coerce"
    )

    # Remove records with invalid dates.
    data = data.dropna(subset=["Date"])

    # Group the reported cases by month.
    monthly_data = (
        data.groupby(
            data["Date"].dt.to_period("M")
        )["Reported_Cases"]
        .sum()
    )

    # Create the figure.
    plt.figure(figsize=(12, 6))

    # Create the line chart.
    plt.plot(
        monthly_data.index.astype(str),
        monthly_data.values,
        marker="o"
    )

    # Add chart details.
    plt.title("Monthly Reported Crime Cases")
    plt.xlabel("Month")
    plt.ylabel("Total Reported Cases")
    plt.xticks(rotation=45)

    plt.tight_layout()

    # Save the chart.
    plt.savefig(
        output_folder / "monthly_crime_trend.png",
        dpi=300
    )

    plt.close()

    print("Monthly crime trend chart saved successfully.")


def main():
    """
    Load the cleaned dataset and generate all three charts.
    """

    # Find the main project directory.
    project_root = Path(__file__).resolve().parent.parent

    # Locate the cleaned dataset.
    input_path = (
        project_root /
        "output" /
        "cleaned_crime_data.csv"
    )

    # Locate the output directory.
    output_folder = project_root / "output"

    # Ensure the output folder exists.
    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    # Load the cleaned dataset.
    crime_data = load_dataset(input_path)

    print("Dataset loaded for visualization.")

    # Generate all three charts.
    create_crime_type_chart(
        crime_data,
        output_folder
    )

    create_victim_age_histogram(
        crime_data,
        output_folder
    )

    create_monthly_crime_chart(
        crime_data,
        output_folder
    )

    print("\nAll visualizations generated successfully!")


if __name__ == "__main__":
    main()
