import re

from util import read_input
from typing import Dict, List


def format_input(raw_info: List[str]) -> Dict[int, List[Dict[str, int]]]:
    id_to_game_data = {}
    for line in raw_info:
        game, raw_data = line.split(":")
        raw_data = raw_data.strip()
        
        game_id = re.search(r'Game ([0-9]+)', game).group(1)

        data_list = []
        for reveal in raw_data.split(";"):
            reveal = reveal.strip()
            reveal_data = {}
            for cubes_info in reveal.split(","):
                cubes_info = cubes_info.strip()
                num, colour = cubes_info.split()
                reveal_data[colour] = int(num)
            data_list.append(reveal_data)
        
        id_to_game_data[int(game_id)] = data_list
    
    return id_to_game_data


def cube_conundrum(id_to_data: Dict[int, List[Dict[str, int]]], max_red: int, max_green: int, max_blue: int) -> int:
    valid_game_ids = set()
    for id, game in id_to_data.items():
        is_game_valid = True
        for reveal in game:
            valid_red = "red" not in reveal or reveal["red"] <= max_red
            valid_green = "green" not in reveal or reveal["green"] <= max_green
            valid_blue = "blue" not in reveal or reveal["blue"] <= max_blue
            if not (valid_red and valid_green and valid_blue):
                is_game_valid = False
                break

        if is_game_valid:
            valid_game_ids.add(id)

    return sum(valid_game_ids)


def cube_conundrum_p2(id_to_data: Dict[int, List[Dict[str,int]]]) -> int:
    cube_powers = []
    for game in id_to_data.values():
        max_red, max_green, max_blue = 0, 0, 0
        for reveal in game:
            max_red = max_red if "red" not in reveal or reveal["red"] <= max_red else reveal["red"]
            max_green = max_green if "green" not in reveal or reveal["green"] <= max_green else reveal["green"]
            max_blue = max_blue if "blue" not in reveal or reveal["blue"] <= max_blue else reveal["blue"]
        
        cube_powers.append(max_red * max_green * max_blue)
    
    return sum(cube_powers)


if __name__ == "__main__":
    sample_input = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    raw_game_info = read_input("inputs/cube_conundrum.txt")
    id_to_game_data = format_input(raw_game_info)
    result_p1 = cube_conundrum(id_to_game_data, 12, 13, 14)
    print(result_p1)
    result_p2 = cube_conundrum_p2(id_to_game_data)
    print(result_p2)
