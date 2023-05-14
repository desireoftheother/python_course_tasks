from pathlib import Path
from os import getcwd

current_working_directory = getcwd()
base_path = Path(current_working_directory).parent

with open(base_path / "titanic_data/titanic_data.csv") as f:
    rows = f.readlines()

cleaned_rows = map(lambda x: x.replace("\n", ""), rows)
splitted_rows = map(lambda s: s.split(","), cleaned_rows)
deleted_second_column = map(lambda l: l[:1] + l[3:], splitted_rows)

with open(base_path / "titanic_data/titanic_data_2.csv", "w") as f:
    for line in deleted_second_column:
        f.write(",".join(line) + "\n")
