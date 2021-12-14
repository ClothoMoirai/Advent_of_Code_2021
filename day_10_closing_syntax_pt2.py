import re
from statistics import median

input_file = 'day_10.txt'
chars = { '[': ']', '{': '}', '(': ')', '<': '>'}
values = { ')': 1, ']': 2, '}': 3, '>': 4}


def get_input(input_file: str) -> list:
    with open(input_file) as syntaxfile:
        syntaxlines = syntaxfile.read().splitlines()
    syntaxfile.close()
    return syntaxlines


def find_pairs(thisline: list) -> str:
    badchar = ''
    prefix = []
    completion = []
    while len(thisline) > 0 and badchar == '':
        if thisline[0] in chars.keys():
            # opening character
            prefix.append(thisline.pop(0))
        elif thisline[0] in chars.values():
            # closing character
            if thisline[0] == chars[prefix[-1]]:
                thisline.pop(0)
                prefix.pop(-1)
            else:
                badchar = thisline[0]
    while len(prefix) > 0 and len(badchar) == 0:
        # if there are still prefix characters and no bad characters this is an imcomplete line.
        completion.append(chars[prefix.pop(-1)])
    return completion


def process_syntaxlines(syntaxlines: list) -> list:
    completioncharacters = []
    while len(syntaxlines) > 0:
        thisline = list(syntaxlines.pop(0))
        completion = find_pairs(thisline)
        if len(completion) > 0:
            completioncharacters.append(completion)
    return completioncharacters


def compute_total(completion: list) -> int:
    totals = []
    for i in completion:
        thistotal = 0
        for x in i:
            thistotal *= 5
            thistotal += values[x]
        totals.append(thistotal)
    totals.sort()
    return median(totals)


def main(input_file: str) -> None:
    syntaxlines = get_input(input_file)
    offendingsyntax = process_syntaxlines(syntaxlines)
    print(compute_total(offendingsyntax))
    return


main(input_file)
