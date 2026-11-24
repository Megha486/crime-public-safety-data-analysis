
import sys
from pathlib import Path

import pandas as pd

# Add the src folder to Python's search path.
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from data_visualization import (
    create_crime_type_chart,
    create_victim_age_histogram,
    create_monthly_crime_chart
)


def test_create_crime_type_chart(tmp_path):

    data = {
        "Crime_Type": [
            "Theft",
            "Robbery",
            "Theft",
            "Assault"
        ]
    }

    df = pd.DataFrame(data)

    create_crime_type_chart(df, tmp_path)

    assert (
        tmp_path / "crime_type_distribution.png"
    ).exists()


def test_create_victim_age_histogram(tmp_path):

    data = {
        "Victim_Age": [20, 25, 30, 35, 40, 45]
    }

    df = pd.DataFrame(data)

    create_victim_age_histogram(df, tmp_path)

    assert (
        tmp_path / "victim_age_distribution.png"
    ).exists()


def test_create_monthly_crime_chart(tmp_path):

    data = {
        "Date": [
            "2025-01-10",
            "2025-01-15",
            "2025-02-10",
            "2025-03-20"
        ],
        "Reported_Cases": [10, 15, 20, 25]
    }

    df = pd.DataFrame(data)

    create_monthly_crime_chart(df, tmp_path)

    assert (
        tmp_path / "monthly_crime_trend.png"
    ).exists()


def test_all_charts_are_generated(tmp_path):

    data = {
        "Crime_Type": [
            "Theft",
            "Robbery",
            "Assault"
        ],
        "Victim_Age": [20, 30, 40],
        "Date": [
            "2025-01-10",
            "2025-02-10",
            "2025-03-10"
        ],
        "Reported_Cases": [10, 20, 30]
    }

    df = pd.DataFrame(data)

    create_crime_type_chart(df, tmp_path)
    create_victim_age_histogram(df, tmp_path)
    create_monthly_crime_chart(df, tmp_path)

    assert (
        tmp_path / "crime_type_distribution.png"
    ).exists()

    assert (
        tmp_path / "victim_age_distribution.png"
    ).exists()

    assert (
        tmp_path / "monthly_crime_trend.png"
    ).exists()
