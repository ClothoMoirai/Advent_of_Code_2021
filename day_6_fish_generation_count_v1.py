from typing import List
import re

generations = 80

def get_input(myfile: str) -> list:
    with open(myfile, 'r') as fishfile:
        fishlist = [int(x) for x in re.sub('\n', '', fishfile.read()).split(',')]
    fishfile.close()
    return fishlist


def compute_generations(fishlist: list, generations: int) -> list:
    for i in range(generations):
        for x in range(len(fishlist)):
            if fishlist[x] == 0:
                fishlist.append(8)
                fishlist[x] = 6
            else:
                fishlist[x] -= 1
    return fishlist



def main():
    fishlist = get_input('day_6.txt')
    fishlist = compute_generations(fishlist, generations)
    print(len(fishlist))


main()