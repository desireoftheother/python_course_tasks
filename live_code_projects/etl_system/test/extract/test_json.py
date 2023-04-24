import pytest
import pathlib

from live_code_projects.etl_system.src.extract.json import JSONExtractor


@pytest.fixture
def json_path(cwd) -> pathlib.Path:
    test_data_path = cwd / "extract/test_data/json_data.json"
    return test_data_path


@pytest.fixture
def json_extractor(json_path) -> JSONExtractor:
    return JSONExtractor(json_path)


def test__process_file_format(json_extractor) -> None:
    assert json_extractor.extract()[0]["PassengerId"] == "892"
