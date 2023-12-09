# Day 08 -- December 8, 2023

import copy

from util import read_input
from typing import Dict, List


class Map:
    def __init__(self, directions: str, neighbours: Dict[str, List[str]], a_nodes: List[str]):
        self.directions = directions.strip()
        self.neighbours = neighbours
        self.a_nodes = a_nodes

    def find_num_steps(self) -> int:
        num_steps = 0
        i = 0
        current_node = "AAA"
        while current_node != "ZZZ":
            if i == len(self.directions):
                i = 0
            
            direction = 0 if self.directions[i] == "L" else 1
            current_node = self.neighbours[current_node][direction]
            num_steps += 1
            i += 1

        return num_steps
    
    def find_ghost_steps(self) -> int:
        num_steps = 0
        i = 0
        curr_nodes = copy.copy(self.a_nodes)
        while True:
            num_steps += 1
            if i == len(self.directions):
                i = 0
            
            direction = 0 if self.directions[i] == "L" else 1
            end_nodes = [self.neighbours[node][direction] for node in curr_nodes]
            z_nodes = list(filter(lambda x: x.endswith("Z"), end_nodes))

            if len(end_nodes) == len(z_nodes):
                return num_steps
            
            curr_nodes = end_nodes
            i += 1



class Solver:
    def __init__(self, raw_data: List[str]):
        self.directions = raw_data[0]
        self.neighbours = {}
        self.a_nodes = []

        for i in range(2, len(raw_data)):
            line = raw_data[i]
            node, neighbours = line.split(" = ")
            neighbours = neighbours[1:len(neighbours) - 2].split(", ")

            self.neighbours[node] = neighbours

            if node.endswith("A"):
                self.a_nodes.append(node)

    def solve_p1(self) -> int:
        map = Map(self.directions, self.neighbours, self.a_nodes)
        return map.find_num_steps()
    
    def solve_p2(self) -> int:
        map = Map(self.directions, self.neighbours, self.a_nodes)
        return map.find_ghost_steps()


if __name__ == "__main__":
    sample_data_1 = [
        "RL",
        "",
        "AAA = (BBB, CCC)\n",
        "BBB = (DDD, EEE)\n",
        "CCC = (ZZZ, GGG)\n",
        "DDD = (DDD, DDD)\n",
        "EEE = (EEE, EEE)\n",
        "GGG = (GGG, GGG)\n",
        "ZZZ = (ZZZ, ZZZ)\n",
    ]
    sample_data_2 = [
        "LLR",
        "",
        "AAA = (BBB, BBB)\n",
        "BBB = (AAA, ZZZ)\n",
        "ZZZ = (ZZZ, ZZZ)\n",
    ]
    raw_data = read_input("inputs/haunted_wasteland.txt")
    solver = Solver(raw_data)
    print(solver.solve_p1())

    p2_sample = [
        "LR",
        "",
        "11A = (11B, XXX)\n",
        "11B = (XXX, 11Z)\n",
        "11Z = (11B, XXX)\n",
        "22A = (22B, XXX)\n",
        "22B = (22C, 22C)\n",
        "22C = (22Z, 22Z)\n",
        "22Z = (22B, 22B)\n",
        "XXX = (XXX, XXX)\n",
    ]
    solver = Solver(raw_data)
    print(solver.solve_p2())
