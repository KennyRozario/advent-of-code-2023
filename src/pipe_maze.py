# Day 10 -- December 10, 2023

from enum import Enum
from util import read_input
from typing import List, Tuple, Optional


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class Maze:
    def __init__(self, maze_data: List[List[str]], starting_position: Tuple[int, int]):
        self.maze_data = maze_data
        self.starting_position = starting_position

    def next_pos(self, position: Tuple[int, int], from_dir: Direction) -> Optional[List[int]]:
        """
        Returns None if current position is invalid (coordinates or ground type) or cannot access the current type from previous direction
        Returns List[positon[row], position[col], from_dir if this route is taken from current position]
        """
        if position[0] < 0 or position[0] >= len(self.maze_data) or position[1] < 0 or position[1] >= len(self.maze_data[0]):
            return None

        current_pipe_type = self.maze_data[position[0]][position[1]]
        if current_pipe_type == "|" and (from_dir == Direction.NORTH or from_dir == Direction.SOUTH):
            return [position[0] + 1, position[1], Direction.NORTH] if from_dir == Direction.NORTH else [position[0] - 1, position[1], Direction.SOUTH]
        elif current_pipe_type == "-" and (from_dir == Direction.EAST or from_dir == Direction.WEST):
            return [position[0], position[1] + 1, Direction.WEST] if from_dir == Direction.WEST else [position[0], position[1] - 1, Direction.EAST]
        elif current_pipe_type == "L" and (from_dir == Direction.NORTH or from_dir == Direction.EAST):
            return [position[0], position[1] + 1, Direction.WEST] if from_dir == Direction.NORTH else [position[0] - 1, position[1], Direction.SOUTH]
        elif current_pipe_type == "J" and (from_dir == Direction.NORTH or from_dir == Direction.WEST):
            return [position[0], position[1] - 1, Direction.EAST] if from_dir == Direction.NORTH else [position[0] - 1, position[1], Direction.SOUTH]
        elif current_pipe_type == "7" and (from_dir == Direction.WEST or from_dir == Direction.SOUTH):
            return [position[0], position[1] - 1, Direction.EAST] if from_dir == Direction.SOUTH else [position[0] + 1, position[1], Direction.NORTH]
        elif current_pipe_type == "F" and (from_dir == Direction.EAST or from_dir == Direction.SOUTH):
            return [position[0], position[1] + 1, Direction.WEST] if from_dir == Direction.SOUTH else [position[0] + 1, position[1], Direction.NORTH]
        else:
            return None
    
    def find_steps_to_furthest_point(self) -> int:
        directions = [
            self.next_pos((self.starting_position[0] - 1, self.starting_position[1]), Direction.SOUTH),
            self.next_pos((self.starting_position[0], self.starting_position[1] + 1), Direction.WEST),
            self.next_pos((self.starting_position[0] + 1, self.starting_position[1]), Direction.NORTH),
            self.next_pos((self.starting_position[0], self.starting_position[1] - 1), Direction.EAST),
        ]
        directions = [direction for direction in directions if direction]
        first_dir, second_dir = directions[0], directions[1]

        steps_taken = 1
        while True:
            steps_taken += 1
            if first_dir[0] == second_dir[0] and first_dir[1] == second_dir[1]:
                break
            
            first_dir = self.next_pos((first_dir[0], first_dir[1]), first_dir[2])
            second_dir = self.next_pos((second_dir[0], second_dir[1]), second_dir[2])

        return steps_taken

        
class Solver:
    def __init__(self, raw_data: List[str]):
        self.maze_data = []
        self.starting_position = (0, 0)

        for idx, line in enumerate(raw_data):
            s_pos = line.find("S")
            if s_pos >= 0:
                self.starting_position = (idx, s_pos)
        
            self.maze_data.append(list(line.strip()))

    def solve_p1(self):
        maze = Maze(self.maze_data, self.starting_position)
        return maze.find_steps_to_furthest_point()


if __name__ == "__main__":
    sample_data = [
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        ".....",
    ]
    sample_data_2 = [
        "-L|F7",
        "7S-7|",
        "L|7||",
        "-L-J|",
        "L|-JF",
    ]
    sample_data_3 = [
        "..F7.",
        ".FJ|.",
        "SJ.L7",
        "|F--J",
        "LJ...",
    ]
    raw_data = read_input("inputs/pipe_maze.txt")
    solver = Solver(raw_data)
    print(solver.solve_p1())
    
