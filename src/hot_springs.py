# Day 12 -- December 12, 2023

from util import read_input
from typing import List

class ConditionRecord:
    def __init__(self, spring_data: str, dmg_group_sizes: List[int]):
        self.spring_data = spring_data
        self.dmg_group_sizes = dmg_group_sizes

    def shrink

    def get_num_arrangements(self) -> int:
        # num_total_arrangements = num_unknown Choose (total_damaged - known_damaged)

        num_arrangements = 0

        group_idx = len(self.dmg_group_sizes) - 1
        while group_idx >= 0:
            group_size = self.dmg_group_sizes[group_idx]


        return num_arrangements

class Solver:
    def __init__(self, raw_data: List[str]):
        data = raw_data.strip().split()
        self.springs = data[0]
        self.dmg_group_sizes = [int(group_size) for group_size in data[1].split(",")]


    def solve_p1(self) -> int:
        condition_records = [ConditionRecord(self.springs[i], self.dmg_group_sizes[i]) for i in range(0, len(self.springs))]
        arrangements = []
        for condition_record in condition_records:
            arrangements.append(condition_record.get_num_arrangements())

        return sum(arrangements)


if __name__ == "__main__":
    sample_data = [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",
    ]
    raw_data = read_input("inputs/hot_springs.txt")
