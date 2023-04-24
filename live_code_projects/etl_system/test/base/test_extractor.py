import pytest
from unittest.mock import patch, mock_open
from live_code_projects.etl_system.src.base.extractor import AbstractExtractor


class MockExtractor(AbstractExtractor):
    def _process_file_format(self, file):
        return self.path + file.read()


@pytest.fixture
def mock_extractor() -> MockExtractor:
    return MockExtractor("some_path/")


def test_extract(mock_extractor):
    with patch("builtins.open", mock_open(read_data="hey")):
        assert mock_extractor.extract() == "some_path/hey"
