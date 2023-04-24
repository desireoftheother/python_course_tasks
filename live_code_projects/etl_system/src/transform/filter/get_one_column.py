from typing import List, Dict, Any

from live_code_projects.etl_system.src.base.transformer import AbstractTransform


class GetOneColumn(AbstractTransform):
    @property
    def __init__(self, input_dataset: List[Dict[Any, Any]], column_name: str):
        self.input_dataset = input_dataset
        self.column_name = column_name

    def transform(self) -> List[Dict[Any, Any]]:
        return [{self.column_name: row[self.column_name]} for row in self.input_dataset]
