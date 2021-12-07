from typing import List
import re

input_file = 'day_7.txt'

def get_input(myfile: str) -> list:
    with open(myfile, 'r') as subfile:
        sublist = [int(x) for x in re.sub('\n', '', subfile.read()).split(',')]
    subfile.close()
    return sublist


def find_best_position(mysubs: list) -> int:
    position_fuel_cost = []
    for i in (range(max(mysubs))):
        position_fuel_cost.append(0)
        for thissub in mysubs:
            if thissub < i:
                position_fuel_cost[i] += (i - thissub)
            else:
                position_fuel_cost[i] += (thissub - i)
    return min(position_fuel_cost)


def main(input_file: str) -> None:
    mysubs = get_input(input_file)
    print(find_best_position(mysubs))

main(input_file)
