# Day 11 -- December 11, 2023

import copy

from util import read_input
from typing import List, Tuple


class Universe:
    def __init__(self, map_data: List[str]):
        self.map_data = map_data
        self.expand_map()
        self.galaxy_coords = self.find_galaxies()

    def expand_map(self) -> None:
        j = 0
        while j < len(self.map_data[0]):
            duplicate_column = True
            for i in range(0, len(self.map_data)):
                if self.map_data[i][j] != ".":
                    duplicate_column = False
                    break
            
            if duplicate_column:
                for i in range(0, len(self.map_data)):
                    self.map_data[i].insert(j, ".")
                j += 1
            j += 1
        
        i = 0
        while i < len(self.map_data):
            row = self.map_data[i]
            duplicate_row = True
            for col in row:
                if col != ".":
                    duplicate_row = False
                    break
            if duplicate_row:
                self.map_data.insert(i, copy.copy(row))
                i += 1
            i += 1

    def find_galaxies(self) -> List[Tuple[int, int]]:
        galaxy_coords = []
        for i in range(0, len(self.map_data)):
            for j in range(0, len(self.map_data[0])):
                if self.map_data[i][j] == "#":
                    galaxy_coords.append((i, j))
        return galaxy_coords
    
    def sum_shortest_paths_between_galaxies(self) -> int:
        distances = []
        for i in range(0, len(self.galaxy_coords)):
            for j in range(i + 1, len(self.galaxy_coords)):
                galaxy_1, galaxy_2 = self.galaxy_coords[i], self.galaxy_coords[j]
                distance = abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1])
                distances.append(distance)
        return sum(distances)
    

class Solver:
    def __init__(self, raw_data: List[str]):
        map_data = [list(line.strip()) for line in raw_data]
        self.universe = Universe(map_data)

    def solve_p1(self) -> int:
        return self.universe.sum_shortest_paths_between_galaxies()


if __name__ == "__main__":
    sample_data = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]
    sample_expanded = [
        "....#........",
        ".........#...",
        "#............",
        ".............",
        ".............",
        "........#....",
        ".#...........",
        "............#",
        ".............",
        ".............",
        ".........#...",
        "#....#.......",
    ]
    raw_data = read_input("inputs/cosmic_expansion.txt")
    solver = Solver(raw_data)
    print(solver.solve_p1())
