import json
from live_code_projects.etl_system.src.base.extractor import AbstractExtractor


class JSONExtractor(AbstractExtractor):
    def _process_file_format(self, file):
        return json.load(file)
