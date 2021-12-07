from typing import List
import re

days = 256
input_file = 'day_6.txt'

def get_input(myfile: str) -> list:
    with open(myfile, 'r') as fishfile:
        fishlist = [int(x) for x in re.sub('\n', '', fishfile.read()).split(',')]
    fishfile.close()
    return fishlist


def compute_generations(fishlist: list, days: int) -> list:
    for i in range(days):
        birthing = fishlist.pop(0)
        fishlist.append(birthing)
        fishlist[6] += birthing
    return fishlist


def process_input(fishinput: list,) -> list:
    fishlist = []
    for i in range(9):
        fishlist.append(0)
    for i in fishinput:
        fishlist[i] += 1
    return fishlist

def main(days: int, input_file: str) -> None:
    fishinput = get_input(input_file)
    fishlist = process_input(fishinput)
    fishlist = compute_generations(fishlist, days)
    print(sum(fishlist))


main(days, input_file)