import pandas as pd
import time

from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from pathlib import Path
from os import getcwd
from ast import literal_eval



CSV_RELATIVE_PATH = f"module_5/35_concurrency_multiprocessing/CSV_FILES/"
STEP = 10000
MAX_ROW_COUNT = 1_000_000

cwd = Path(getcwd())


def read_and_parse(path):
    start = time.time()
    print("Started parsing file: ", path)
    df = pd.read_csv(path, delimiter="|")
    df["parsed_entry"] = df["entry"].apply(literal_eval)
    print("Finished parsing file: ", path)
    end = time.time()
    print(f"Time taken for parsing file {path}: {end-start}")
    return df 

start = time.time()

# with ThreadPoolExecutor(6) as pool:
#     csv_df = pd.concat(list(pool.map(read_and_parse, [cwd/CSV_RELATIVE_PATH/f"output_{i}.csv" for i in range(1, MAX_ROW_COUNT, STEP)])))
    
# with ProcessPoolExecutor(6) as pool:
#     csv_df = pd.concat(list(pool.map(read_and_parse, [cwd/CSV_RELATIVE_PATH/f"output_{i}.csv" for i in range(1, MAX_ROW_COUNT, STEP)])))
    
# csv_df = pd.concat(
#     [read_and_parse(cwd/CSV_RELATIVE_PATH/f"output_{i}.csv") for i in range(1, MAX_ROW_COUNT, STEP)]
# )


end = time.time()

print(f"Time taken: {end-start}")