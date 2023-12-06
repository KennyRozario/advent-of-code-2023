# Day 06 -- December 6, 2023

import math

from util import read_input
from typing import List


class BoatRace:
    def __init__(self, duration, record_distance):
        self.duration = duration
        self.record_distance = record_distance

    def get_successful_hold_durations(self) -> List[int]:
        hold_durations = []
        for hold_duration in range(0, self.duration):
            speed = hold_duration
            distance = (self.duration - hold_duration) * speed
            if distance > self.record_distance:
                hold_durations.append(hold_durations)
        
        return hold_durations
    
    def get_num_successful_hold_duration_p2(self) -> int:
        min_hold = 0
        max_hold = self.duration
        i,j = 1, self.duration - 1
        while i <= j:
            distance_l = (self.duration - i) * i
            distance_r = (self.duration - j) * j

            l_changed = distance_l > self.record_distance
            r_changed = distance_r > self.record_distance
            if l_changed and r_changed:
                min_hold = i
                max_hold = j
                break
            elif l_changed:
                min_hold = i
                j -= 1
            elif r_changed:
                max_hold = j
                i += 1
            else:
                i += 1
                j -= 1

        return max_hold - min_hold + 1



class Solver:
    def __init__(self, raw_data: List[str]):
        self.times = [int(time) for time in raw_data[0].split(":")[1].strip().split()]
        self.distances = [int(distance) for distance in raw_data[1].split(":")[1].strip().split()]
        self.p2_time = int(''.join(raw_data[0].split(":")[1].strip().split()))
        self.p2_distance = int(''.join(raw_data[1].split(":")[1].strip().split()))

    def get_error_margin(self) -> int:
        num_hold_durations = []
        for i in range(0, len(self.times)):
            race = BoatRace(self.times[i], self.distances[i])
            hold_durations = race.get_successful_hold_durations()
            num_hold_durations.append(len(hold_durations))

        return math.prod(num_hold_durations)
    
    def get_error_margin_p2(self) -> int:
        race = BoatRace(self.p2_time, self.p2_distance)
        return race.get_num_successful_hold_duration_p2()
    
    def p2_using_p1(self) -> int:
        race = BoatRace(self.p2_time, self.p2_distance)
        hold_durations = race.get_successful_hold_durations()
        return len(hold_durations)


if __name__ == "__main__":
    sample_data = [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]
    raw_data = read_input("inputs/wait_for_it.txt")
    solver = Solver(raw_data)
    print(solver.get_error_margin())

    print(f"p2 solved with p1: {solver.p2_using_p1()}")
    print(solver.get_error_margin_p2())
