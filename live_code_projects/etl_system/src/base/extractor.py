from abc import ABC, abstractmethod
from typing import List, Dict, Any


class AbstractExtractor(ABC):

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def _process_file_format(self, file):
        pass

    def extract(self) -> List[Dict[Any, Any]]:
        """Main entry point for extract operation.
        This method should perform basic extraction and parsing functionality.
        For example, you can read CSV file, parse all the data from it and return a collection of objects."""
        with open(self.path, "r") as file:
            result = self._process_file_format(file)
            return result
