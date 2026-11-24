
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

# Add the src folder to Python's search path.
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from data_analysis import analyze_data, save_analysis_results


def test_calculate_statistical_summary():
    data = {
        "Victim_Age": [20, 30, 40, 50],
        "Reported_Cases": [10, 20, 30, 40]
    }

    df = pd.DataFrame(data)

    statistics_df, frequencies = analyze_data(df)

    assert len(statistics_df) == 2
    assert "Mean" in statistics_df.columns
    assert "Median" in statistics_df.columns
    assert "Minimum" in statistics_df.columns
    assert "Maximum" in statistics_df.columns


def test_calculate_mean_and_median():
    df = pd.DataFrame({
        "Victim_Age": [20, 30, 40]
    })

    statistics_df, _ = analyze_data(df)

    assert statistics_df.iloc[0]["Mean"] == 30
    assert statistics_df.iloc[0]["Median"] == 30


def test_calculate_standard_deviation():
    df = pd.DataFrame({
        "Victim_Age": [10, 20, 30]
    })

    statistics_df, _ = analyze_data(df)

    expected = np.std([10, 20, 30], ddof=1)

    assert np.isclose(
        statistics_df.iloc[0]["Standard Deviation"],
        expected
    )


def test_categorical_frequency_distribution():
    df = pd.DataFrame({
        "Crime_Type": ["Theft", "Robbery", "Theft", "Theft"],
        "State": ["Assam", "Meghalaya", "Assam", "Assam"]
    })

    statistics_df, frequencies = analyze_data(df)

    assert frequencies["Crime_Type"]["Theft"] == 3
    assert frequencies["State"]["Assam"] == 3


def test_date_column_excluded_from_frequency():
    df = pd.DataFrame({
        "Crime_Date": ["2024-01-01", "2024-01-02"],
        "Crime_Type": ["Theft", "Robbery"]
    })

    statistics_df, frequencies = analyze_data(df)

    assert "Crime_Date" not in frequencies
    assert "Crime_Type" in frequencies


def test_save_analysis_results(tmp_path):
    df = pd.DataFrame({
        "Victim_Age": [20, 30, 40],
        "Crime_Type": ["Theft", "Robbery", "Theft"]
    })

    statistics_df, frequencies = analyze_data(df)

    save_analysis_results(
        statistics_df,
        frequencies,
        tmp_path
    )

    assert (tmp_path / "statistical_summary.csv").exists()
    assert (tmp_path / "frequency_crime_type.csv").exists()


def test_empty_numerical_column():
    df = pd.DataFrame({
        "Victim_Age": [None, None, None]
    })

    statistics_df, frequencies = analyze_data(df)

    assert statistics_df.empty
