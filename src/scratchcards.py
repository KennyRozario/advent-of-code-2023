# Day 04 -- December 4, 2023

import math

from util import read_input
from typing import List


class ScratchCard:
    def __init__(self, id: int, card_data: str):
        self.id = id

        winning_num_data, given_num_data = card_data.split("|")
        self.winning_nums = set([int(winning_num) for winning_num in winning_num_data.strip().split()])
        self.given_nums = set([int(given_num) for given_num in given_num_data.strip().split()])

    def get_num_matches(self):
        return len(self.winning_nums.intersection(self.given_nums))

    def get_points(self) -> int:
        num_winning = self.get_num_matches()
        return 0 if num_winning == 0 else math.pow(2, (num_winning - 1))
    
    def get_id(self) -> int:
        return self.id
    

def get_scratch_cards(raw_card_data: List[str]) -> List[ScratchCard]:
    scratch_cards = []
    for card_data in raw_card_data:
        card_meta, card_nums = card_data.split(":")
        card_id = int(card_meta.strip().split()[1])
        card_nums = card_nums.strip()

        scratch_card = ScratchCard(card_id, card_nums)
        scratch_cards.append(scratch_card)
        
    return scratch_cards


def get_total_points(scratch_cards: List[ScratchCard]) -> int:
    return sum([scratch_card.get_points() for scratch_card in scratch_cards])


def get_total_num_cards(scratch_cards: List[ScratchCard]) -> int:
    card_id_to_winnings = {}
    for card in scratch_cards:
        card_id_to_winnings[card.get_id()] = card.get_num_matches() 

    total_num_cards = len(scratch_cards)
    cards_to_check = list(range(total_num_cards))
    for card_index in cards_to_check:
        card = scratch_cards[card_index]
        total_num_cards += card_id_to_winnings[card.get_id()]
        cards_to_check.extend(list(range(card_index + 1, card_index + card_id_to_winnings[card.get_id()] + 1)))
    
    return total_num_cards


if __name__ == "__main__":
    sample_data = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]
    raw_data = read_input("inputs/scratchcards.txt")
    scratch_cards = get_scratch_cards(raw_data)
    print(get_total_points(scratch_cards))
    print(get_total_num_cards(scratch_cards))
