from abc import ABC, abstractmethod
from typing import List, Dict, Any


class AbstractTransform(ABC):
    @abstractmethod
    def transform(self) -> List[Dict[Any, Any]]:
        pass
