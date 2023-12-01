from typing import List

def read_input(file_name: str) -> List[str]:
    with open(file_name) as f:
        return f.readlines()
