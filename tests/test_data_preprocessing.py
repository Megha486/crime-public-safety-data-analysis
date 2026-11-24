
import sys
from pathlib import Path

import pandas as pd
import pytest

# Add the src folder to Python's search path.
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from data_preprocessing import preprocess_data


def test_remove_duplicates():
    data = {
        "Crime_Type": ["Theft", "Theft", "Robbery"],
        "Victim_Age": [20, 20, 30]
    }

    df = pd.DataFrame(data)

    result = preprocess_data(df)

    assert len(result) == 2


def test_handle_missing_numeric_values():
    data = {
        "Victim_Age": [20, None, 40]
    }

    df = pd.DataFrame(data)

    result = preprocess_data(df)

    assert result["Victim_Age"].isnull().sum() == 0
    assert result["Victim_Age"].iloc[1] == 30


def test_correct_numeric_data_types():
    data = {
        "Victim_Age": ["20", "30", "40"]
    }

    df = pd.DataFrame(data)

    result = preprocess_data(df)

    assert pd.api.types.is_numeric_dtype(
        result["Victim_Age"]
    )


def test_convert_date_column():
    data = {
        "Date": ["2024-01-01", "2024-02-01"]
    }

    df = pd.DataFrame(data)

    result = preprocess_data(df)

    assert pd.api.types.is_datetime64_any_dtype(
        result["Date"]
    )


def test_original_data_remains_unchanged():
    data = {
        "Victim_Age": [20, None, 40],
        "Crime_Type": ["Theft", "Robbery", "Theft"]
    }

    df = pd.DataFrame(data)

    original_df = df.copy(deep=True)

    preprocess_data(df)

    pd.testing.assert_frame_equal(df, original_df)
