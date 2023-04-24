import pytest
import pathlib

from live_code_projects.etl_system.src.extract.csv import CSVExtractor


@pytest.fixture
def csv_path(cwd) -> pathlib.Path:
    test_data_path = cwd / "extract/test_data/csv_data.csv"
    return test_data_path


@pytest.fixture
def csv_extractor(csv_path) -> CSVExtractor:
    return CSVExtractor(csv_path)


def test__process_file_format(csv_extractor) -> None:
    assert csv_extractor.extract()[0]["PassengerId"] == "1"
