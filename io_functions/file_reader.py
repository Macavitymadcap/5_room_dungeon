from pathlib import Path

def line_generator(file_path: Path):
    with open(file_path.as_posix(), 'r') as file:
        for line in file:
            yield line.strip()