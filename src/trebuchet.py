# Day 01 -- December 1, 2023

from util import read_input
from typing import List


def get_value(line: str) -> int:
    if not line:
        return

    i, j = 0, len(line) - 1
    while i <= j:
        first, last = line[i], line[j]
        if first.isdigit() and last.isdigit():
            value = f"{first}{last}"
            return int(value)

        if first.isdigit():
            j -= 1
        elif last.isdigit():
            i += 1
        else:
            i += 1
            j -= 1


def trebuchet(calibration_doc: List[str]) -> int:
    values_to_sum = []
    for line in calibration_doc:
        values_to_sum.append(get_value(line))
    
    return sum(values_to_sum)


def trebuchet_p2(calibration_doc: List[str]) -> int:
    reformatted_doc = []
    word_to_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    letter_to_words = {
        "e": ["eight"],
        "f": ["four", "five"],
        "n": ["nine"],
        "o": ["one"],
        "s": ["six", "seven"],
        "t": ["two", "three"],
    }
    for line in calibration_doc:
        i = 0
        length = len(line)
        new_line = ""
        while i < length:
            if line[i] in letter_to_words:
                for word in letter_to_words[line[i]]:
                    if line.startswith(word, i):
                        new_line += word_to_digit[word]
                        line = line.replace(word, word[-1], 1)
                        length = len(line)
                        i -= 1
            else:
                new_line += line[i]
            i += 1
        reformatted_doc.append(new_line)

    return trebuchet(reformatted_doc)



if __name__ == "__main__":
    input = read_input("inputs/trebuchet.txt")
    result = trebuchet(input)
    print(f"Part 1: {result}")
    result_2 = trebuchet_p2(input)
    print(f"Part 2: {result_2}")
