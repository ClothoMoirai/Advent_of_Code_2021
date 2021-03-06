from typing import List
import re

days = 80

def get_input(myfile: str) -> list:
    with open(myfile, 'r') as fishfile:
        fishlist = [int(x) for x in re.sub('\n', '', fishfile.read()).split(',')]
    fishfile.close()
    return fishlist


def compute_generations(fishlist: list, days: int) -> list:
    for i in range(days):
        for x in range(len(fishlist)):
            if fishlist[x] == 0:
                fishlist.append(8)
                fishlist[x] = 6
            else:
                fishlist[x] -= 1
    return fishlist



def main(days: int) -> None:
    fishlist = get_input('day_6.txt')
    fishlist = compute_generations(fishlist, days)
    print(len(fishlist))


main(days)
