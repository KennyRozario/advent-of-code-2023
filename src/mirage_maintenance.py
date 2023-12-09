# Day 09 -- December 9,2023

from util import read_input
from typing import List

import copy


class History:
    def __init__(self, data: List[int]) -> int:
        self.data = data

    def get_differences(self) -> List[List[int]]:
        differences = []
        i, j = 0, 1
        layer = self.data
        curr_diffs = []
        while True:
            if j == len(layer):
                differences.append(layer)
                if all(x == 0 for x in layer):
                    break
                layer = copy.copy(curr_diffs)
                curr_diffs.clear()
                i, j = 0, 1
            
            curr_diffs.append(layer[j] - layer[i])
            i += 1
            j += 1

        return differences

    def predict_next_entry(self):
        differences = self.get_differences()
        i = len(differences) - 2
        next = 0
        while i >= 0:
            next = differences[i][-1] + next
            i -= 1
        
        print(f"{self.data} -> {next}")
        return next
    
    def predict_earlier_entry(self):
        differences = self.get_differences()
        i = len(differences) - 2
        prev = 0
        while i >= 0:
            prev = differences[i][0] - prev
            i -= 1
        
        print(f"{self.data} -> {prev}")
        return prev


class Solver:
    def __init__(self, raw_data: List[str]):
        self.histories = []
        for line in raw_data:
            self.histories.append(History([int(x) for x in line.strip().split()]))
    
    def get_prediction_sum(self) -> int:
        return sum([history.predict_next_entry() for history in self.histories])
    
    def get_early_prediction_sum(self) -> int:
        return sum([history.predict_earlier_entry() for history in self.histories])
        


if __name__ == "__main__":
    sample_data = [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45",
    ]
    raw_data = read_input("inputs/mirage_maintenance.txt")
    solver = Solver(raw_data)
    print(solver.get_prediction_sum())
    print(solver.get_early_prediction_sum())
