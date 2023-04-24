import os
import pathlib

import pytest


@pytest.fixture
def cwd() -> pathlib.Path:
    return pathlib.Path(os.path.dirname(__file__))
