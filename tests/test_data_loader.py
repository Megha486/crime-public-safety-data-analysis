

import sys
from pathlib import Path

import pandas as pd
import pytest

# Add the src folder to Python's search path.
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from data_loader import load_dataset



def test_load_csv_successfully(tmp_path):
    file_path = tmp_path / "test.csv"

    data = {
        "Crime_Type": ["Theft", "Robbery"],
        "State": ["Meghalaya", "Assam"]
    }

    pd.DataFrame(data).to_csv(file_path, index=False)

    result = load_dataset(file_path)

    assert len(result) == 2
    assert "Crime_Type" in result.columns


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_dataset("missing_file.csv")


def test_unsupported_file_format(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Sample data")

    with pytest.raises(ValueError):
        load_dataset(file_path)


def test_load_json_successfully(tmp_path):
    file_path = tmp_path / "test.json"

    data = {"Crime_Type": ["Theft", "Robbery"]}
    pd.DataFrame(data).to_json(file_path)

    result = load_dataset(file_path)

    assert len(result) == 2


def test_empty_csv(tmp_path):
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")

    with pytest.raises(ValueError):
        load_dataset(file_path)
