from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from os import getcwd
from json import load, dumps
import time
from threading import get_ident


JSON_RELATIVE_PATH = "module_5/34_concurrency_threading/template.json"
CSV_RELATIVE_PATH = "module_5/35_concurrency_multiprocessing/CSV_FILES/"
STEP = 10_000
MAX_ROW_COUNT = 1_000_000

cwd = Path(getcwd())

json_template = load(open(cwd / JSON_RELATIVE_PATH))

def assemble_csv_row(index) -> str:
    return f"{index}|{dumps(json_template)}\n"

def assemble_csv_chunk(starting_index) -> None:
    #print(f"Thread {get_ident()} started generating of chunk {starting_index}; {starting_index + STEP}")
    with open(cwd/CSV_RELATIVE_PATH/f"output_{starting_index}.csv", "w") as csv_file:
        csv_file.write("index|entry\n")        
        for i in range(starting_index, starting_index+STEP):
            csv_file.write(assemble_csv_row(index=i))

start = time.time()
with ProcessPoolExecutor(16) as executor:
    executor.map(assemble_csv_chunk, range(1, MAX_ROW_COUNT, STEP))

# for starting_index in range(1, MAX_ROW_COUNT, STEP):
#     assemble_csv_chunk(starting_index)

end = time.time()

print(f"Time taken: {end-start}")
