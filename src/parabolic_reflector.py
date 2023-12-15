# Day 14 -- December 14, 2023

from util import read_input
from typing import List


class Platform:
    def __init__(self, positions: List[str]):
        self.positions = positions

    def calculate_load(self) -> int:
        total_load = 0
        for j in range(0, len(self.positions[0])):
            column_load = 0
            load_to_add = len(self.positions)

            for i in range(0, len(self.positions)):
                curr = self.positions[i][j]
                if curr == "O":
                    column_load += load_to_add
                    load_to_add -= 1
                elif curr == ".":
                    continue
                else:
                    load_to_add = len(self.positions) - i - 1
            
            total_load += column_load
        
        return total_load


class Solver:
    def __init__(self, raw_data: List[str]):
        self.positions = [list(line.strip()) for line in raw_data]

    def solve_p1(self) -> int:
        platform = Platform(self.positions)
        return platform.calculate_load()


if __name__ == "__main__":
    sample_data = [
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ]

    spaces, tags, rocks = 0,0,0

    raw_data = read_input("inputs/parabolic_reflector.txt")
    for line in raw_data:
        for char in line:
            if char == ".":
                spaces += 1
            elif char == "#":
                tags += 1
            else:
                rocks += 1

    print(spaces)
    print(tags)
    print(rocks)
    solver = Solver(raw_data)
    print(solver.solve_p1())
