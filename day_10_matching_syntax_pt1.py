import re

input_file = 'day_10.txt'
chars = { '[': ']', '{': '}', '(': ')', '<': '>'}
values = { ')': 3, ']': 57, '}': 1197, '>': 25137}


def get_input(input_file: str) -> list:
    with open(input_file) as syntaxfile:
        syntaxlines = syntaxfile.read().splitlines()
    syntaxfile.close()
    return syntaxlines


def find_pairs(thisline: list) -> str:
    badchar = ''
    prefix = []
    while len(thisline) > 0 and badchar == '':
        print(prefix, "----", thisline)
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
    return badchar


def process_syntaxlines(syntaxlines: list) -> list:
    offendingcharacters = []
    while len(syntaxlines) > 0:
        thisline = list(syntaxlines.pop(0))
        badchar = find_pairs(thisline)
        if len(badchar) > 0:
            offendingcharacters.append(badchar)
    return offendingcharacters


def compute_total(badchars: list) -> int:
    total = 0
    for i in badchars:
        total += values[i]
    return total


def main(input_file: str) -> None:
    syntaxlines = get_input(input_file)
    offendingsyntax = process_syntaxlines(syntaxlines)
    print(compute_total(offendingsyntax))
    return


main(input_file)
