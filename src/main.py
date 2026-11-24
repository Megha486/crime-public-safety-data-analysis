
"""
Main execution file for the Crime and Public Safety
Data Analysis System.
"""

from pathlib import Path

from data_loader import load_dataset
from data_preprocessing import preprocess_data
from data_analysis import analyze_data, save_analysis_results

from data_visualization import (
    create_crime_type_chart,
    create_victim_age_histogram,
    create_monthly_crime_chart
)


def main():

    print("=" * 60)
    print(" CRIME AND PUBLIC SAFETY DATA ANALYSIS SYSTEM")
    print("=" * 60)

    # Locate project directory.
    project_root = Path(__file__).resolve().parent.parent

    # Define dataset and output paths.
    input_path = project_root / "data" / "crime_data.csv"
    output_folder = project_root / "output"

    output_folder.mkdir(parents=True, exist_ok=True)

    # STEP 1: Load dataset.
    print("\nSTEP 1: Loading dataset...")

    crime_data = load_dataset(input_path)

    print("Dataset loaded successfully!")
    print("Total records:", len(crime_data))

    # STEP 2: Preprocess dataset.
    print("\nSTEP 2: Preprocessing dataset...")

    cleaned_data = preprocess_data(crime_data)

    cleaned_path = output_folder / "cleaned_crime_data.csv"

    cleaned_data.to_csv(cleaned_path, index=False)

    print("Cleaned dataset saved successfully!")

    # STEP 3: Perform data analysis.
    print("\nSTEP 3: Performing statistical analysis...")

    statistics, frequencies = analyze_data(cleaned_data)

    print("\nStatistical Summary:")
    print(statistics.round(2).to_string(index=False))

    save_analysis_results(
        statistics,
        frequencies,
        output_folder
    )

    # STEP 4: Generate visualizations.
    print("\nSTEP 4: Generating visualizations...")

    create_crime_type_chart(cleaned_data, output_folder)

    create_victim_age_histogram(cleaned_data, output_folder)

    create_monthly_crime_chart(cleaned_data, output_folder)

    # STEP 5: Display completion message.
    print("\n" + "=" * 60)
    print(" DATA ANALYSIS COMPLETED SUCCESSFULLY!")
    print("=" * 60)

    print("\nGenerated output files are available in:")
    print(output_folder)


if __name__ == "__main__":
    main()
