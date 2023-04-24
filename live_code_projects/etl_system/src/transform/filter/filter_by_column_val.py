from typing import List, Dict, Any

from live_code_projects.etl_system.src.base.transformer import AbstractTransform


class FilterByColumnValues(AbstractTransform):
    def __init__(self, input_dataset: List[Dict[Any, Any]], column_name_to_value: Dict[str, Any]):
        self.input_dataset = input_dataset
        self.column_name_to_value = column_name_to_value

    def transform(self) -> List[Dict[Any, Any]]:
        return [
            row for row in self.input_dataset if all(map(
                lambda key: row[key] == self.column_name_to_value[key],
                self.column_name_to_value.keys()
            ))]
