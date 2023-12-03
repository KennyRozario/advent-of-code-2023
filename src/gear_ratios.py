# Day 03 -- December 3, 2023

from copy import deepcopy
from math import prod
from util import read_input
from typing import List, Set

import re


def format_data_to_schematic(raw_data: List[str]) -> List[List[str]]:
    return [[char for char in line] for line in raw_data]


class Engine:
    def __init__(self, schematic: List[List[str]]):
        self.schematic = schematic

    def get_sum_of_part_numbers(self):
        schematic_reader = SchematicReader(self.schematic)
        return sum(schematic_reader.get_all_part_numbers())
    
    def get_sum_of_gear_ratios(self):
        schematic_reader = SchematicReader(self.schematic)
        return sum(schematic_reader.get_gear_ratios())


class SchematicReader:
    def __init__(self, schematic: List[List[str]]):
        self.schematic = deepcopy(schematic)
        self.num_rows = len(self.schematic)
        self.num_cols = len(self.schematic[0])

    def parse_part_number(self, row: int, col: int) -> int:
        left = ""
        current = self.schematic[row][col]
        right = ""

        j = col - 1
        while j >= 0 and self.schematic[row][j].isdigit():
            left = self.schematic[row][j] + left
            self.schematic[row][j] = '.'
            j -= 1
        
        j = col + 1
        while j < self.num_cols and self.schematic[row][j].isdigit():
            right = right + self.schematic[row][j]
            self.schematic[row][j] = '.'
            j += 1
        
        part_number = left + current + right
        return int(part_number)

    def find_adjacent_part_numbers(self, row: int, col: int) -> List[int]:
        part_numbers = []
        for i in (row - 1, row, row + 1):
            if i < 0 or i >= self.num_rows:
                continue
            for j in (col - 1, col, col + 1):
                if j < 0 or j > self.num_cols:
                    continue
                
                if self.schematic[i][j].isdigit():
                    part_number = self.parse_part_number(i, j)
                    part_numbers.append(part_number)
                    self.schematic[i][j] = '.'

        return part_numbers
    
    def get_all_symbols(self) -> Set[str]:
        symbol_regex = r"([^\w\d\s_.])"
        symbols = set()
        for row in range(0, self.num_rows):
            symbols.update(re.findall(symbol_regex, ''.join(self.schematic[row])))

        return symbols
    
    def get_all_part_numbers(self) -> List[int]:
        symbols = self.get_all_symbols()
        part_numbers = []
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                if self.schematic[row][col] in symbols:
                    part_numbers.extend(self.find_adjacent_part_numbers(row, col))

        return part_numbers
    
    def get_gear_ratios(self) -> List[int]:
        gear_symbol = '*'
        gear_ratios = []
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                if self.schematic[row][col] == gear_symbol:
                    part_numbers = self.find_adjacent_part_numbers(row, col)
                    if len(part_numbers) == 2:
                        gear_ratios.append(prod(part_numbers))
        return gear_ratios


if __name__ == "__main__":
    sample_schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    raw_data = read_input("inputs/gear_ratios.txt")
    raw_schematic = format_data_to_schematic(raw_data)
    engine = Engine(raw_schematic)
    print(engine.get_sum_of_part_numbers())
    print(engine.get_sum_of_gear_ratios())
