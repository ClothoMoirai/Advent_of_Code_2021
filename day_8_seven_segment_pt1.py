from typing import List
import re

input_file = 'day_8.txt'


def get_input(myfile: str) -> list:

    with open(myfile, 'r') as subfile:
        sublist = [re.sub('\n', '', x).split('|')[1].lstrip().split() for x in subfile.readlines()]
    subfile.close()
    return sublist


def count_unique_digits(sevensegements:list) -> int:
    uniquelengths = [2, 3, 4, 7]
    count = 0
    for i in sevensegements:
        for x in i:
            if len(x) in uniquelengths:
                count += 1
    return count


def main(input_file: str) -> None:
    sevensegments = get_input(input_file)
    print(count_unique_digits(sevensegments))

main(input_file)
