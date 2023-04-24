from functools import partial
from typing import List, Dict, Any, Callable

from live_code_projects.etl_system.src.base.transformer import AbstractTransform


class FilterOneDatasetByAnother(AbstractTransform):
    def __init__(self, main_dataset: List[Dict[Any, Any]],
                 filter_dataset: List[Dict[Any, Any]],
                 predicate: Callable):
        self.main_dataset = main_dataset
        self.filter_dataset = filter_dataset
        self.predicate = partial(predicate, filter=filter_dataset)

    def transform(self) -> List[Dict[Any, Any]]:
        result = list(filter(self.predicate, self.main_dataset))
        return result
