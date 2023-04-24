import csv
from live_code_projects.etl_system.src.base.extractor import AbstractExtractor


class CSVExtractor(AbstractExtractor):
    def _process_file_format(self, file):
        return list(csv.DictReader(file))
