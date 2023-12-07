# Day 07 -- December 7, 2023

from util import read_input
from typing import Dict, List


class Hand:
    def __init__(self, cards: str, bid: int, p2_flag: bool):
        self.cards = cards
        self.bid = bid
        self.p2_flag = p2_flag

        type_to_count = {}
        for card in self.cards:
            if card in type_to_count:
                type_to_count[card] += 1
            else:
                type_to_count[card] = 1
        
        distribution = sorted(list(type_to_count.values()))
        if (self.p2_flag and 'J' not in self.cards) or not self.p2_flag:
            if distribution == [5]:
                self.type = "FIVE_OF_A_KIND"
            elif distribution == [1, 4]:
                self.type = "FOUR_OF_A_KIND"
            elif distribution == [2, 3]:
                self.type = "FULL_HOUSE"
            elif distribution == [1, 1, 3]:
                self.type = "THREE_OF_A_KIND"
            elif distribution == [1, 2, 2]:
                self.type = "TWO_PAIR"
            elif distribution == [1, 1, 1, 2]:
                self.type = "ONE_PAIR"
            else:
                self.type = "HIGH_CARD"
        else:
            self.set_type_with_jokers(distribution, type_to_count)

    def set_type_with_jokers(self, distribution: int, type_to_count: Dict[str, int]):
        if distribution == [5] or distribution == [1, 4] or distribution == [2, 3]:
            self.type = "FIVE_OF_A_KIND"
        elif distribution == [1, 1, 3]:
            self.type = "FOUR_OF_A_KIND"
        elif distribution == [1, 2, 2] and type_to_count['J'] == 1:
            self.type = "FULL_HOUSE"
        elif distribution == [1, 2, 2] and type_to_count['J'] == 2:
            self.type = "FOUR_OF_A_KIND"
        elif distribution == [1, 1, 1, 2]:
            self.type = "THREE_OF_A_KIND"
        else:
            self.type = "ONE_PAIR"

    def is_stronger(self, other: 'Hand') -> bool:
        for i in range(0, len(self.cards)):
            val, other_val = self.cards[i], other.cards[i]
            if val == other_val:
                continue

            if self.p2_flag:
                card_types = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
            else:
                card_types = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

            for card_type in card_types:
                if val == card_type or other_val == card_type:
                    return val == card_type
        return False


class Solver:
    def __init__(self, raw_data: List[str], p2_flag=False):
        self.num_hands = len(raw_data)
        self.hands = {
            "FIVE_OF_A_KIND": [],
            "FOUR_OF_A_KIND": [],
            "FULL_HOUSE": [],
            "THREE_OF_A_KIND": [],
            "TWO_PAIR": [],
            "ONE_PAIR": [],
            "HIGH_CARD": [],
        }
        self.p2_flag = p2_flag

        for line in raw_data:
            cards, bid = line.split()
            hand = Hand(cards, int(bid), self.p2_flag)
            self.insert_hand(hand, self.hands[hand.type])
        
    def insert_hand(self, new_hand: 'Hand', hands: List['Hand']) -> None:
        for i, hand in enumerate(hands):
            if new_hand.is_stronger(hand):
                hands.insert(i, new_hand)
                return
        
        hands.append(new_hand)

    def get_total_winnings(self) -> int:
        rank = self.num_hands
        total_winnings = 0
        for hand_type in ["FIVE_OF_A_KIND", "FOUR_OF_A_KIND", "FULL_HOUSE", "THREE_OF_A_KIND", "TWO_PAIR", "ONE_PAIR", "HIGH_CARD"]:
            for hand in self.hands[hand_type]:
                total_winnings += hand.bid * rank
                rank -= 1
        
        return total_winnings


if __name__ == "__main__":
    sample_data = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]
    raw_data = read_input("inputs/camel_cards.txt")
    solver = Solver(raw_data)
    print(solver.get_total_winnings())

    solver = Solver(raw_data, True)
    print(solver.get_total_winnings())
