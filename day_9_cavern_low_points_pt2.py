from pprint import pprint
from typing import List
import re

input_file = 'day_9.txt'


def make_basin_grid(cavern_basin_input: list) -> dict:
    cavern_basin = {}
    count = 0
    for i in cavern_basin_input:
        for x in range(len(i)):
            cavern_basin[count] = [int(x) for x in i]
        count += 1
    return cavern_basin


def get_input(myfile: str) -> list:
    with open(myfile, 'r') as cavernfile:
        cavern_basin_input = cavernfile.read().splitlines()
    cavernfile.close()
    return cavern_basin_input


def find_minimums_corners(cavern_basin: dict) -> list:
    minimums = []
    maxrow = max(cavern_basin.keys())
    maxcolumn = len(cavern_basin[0]) - 1
    # row, column, adjacent row, adjacent column
    corners = [[0, 0, 1, 1], [0, maxcolumn, 1, (maxcolumn -1)], \
               [maxrow, 0, (maxrow - 1), 1], \
               [maxrow, maxcolumn, (maxrow -1), (maxcolumn - 1)]]
    for i in corners:
        if (cavern_basin[i[0]][i[1]] < cavern_basin[i[0]][i[3]]) and \
            (cavern_basin[i[0]][i[1]] < cavern_basin[i[2]][i[1]]):
            minimums.append([i[0], i[1]])
    return minimums


def find_minimums_edge(cavern_basin: dict) -> list:
    minimums = []
    maxrow = max(cavern_basin.keys())
    maxcolumn = len(cavern_basin[0]) - 1
    for i in range(1,maxcolumn):
        if (cavern_basin[0][i] < cavern_basin[0][i - 1]) and \
                (cavern_basin[0][i] < cavern_basin[0][i + 1]) and \
                (cavern_basin[0][i] < cavern_basin[1][i]):
            minimums.append([0, i])
        if (cavern_basin[maxrow][i] < cavern_basin[maxrow][i - 1]) and \
                (cavern_basin[maxrow][i] < cavern_basin[maxrow][i + 1]) and \
                (cavern_basin[maxrow][i] < cavern_basin[maxrow - 1][i]):
            minimums.append([maxrow, i])
    for i in range(1,maxrow):
        if (cavern_basin[i][0] < cavern_basin[i - 1][0]) and \
                (cavern_basin[i][0] < cavern_basin[i + 1][0]) and \
                (cavern_basin[i][0] < cavern_basin[i][1]):
            minimums.append([i, 0])
        if (cavern_basin[i][maxcolumn] < cavern_basin[i - 1][maxcolumn]) and \
                (cavern_basin[i][maxcolumn] < cavern_basin[i + 1][maxcolumn]) and \
                (cavern_basin[i][maxcolumn] < cavern_basin[i][maxcolumn - 1]):
            minimums.append([i, maxcolumn])
    return minimums


def find_minimums_center(cavern_basin: dict) -> list:
    minimums = []
    maxrow = max(cavern_basin.keys())
    maxcolumn = len(cavern_basin[0]) - 1
    for x in range(1, maxrow ):
        for y in range(1, maxcolumn):
            if (cavern_basin[x][y] < cavern_basin[x - 1][y]) and \
                    (cavern_basin[x][y] < cavern_basin[x + 1][y]) and \
                    (cavern_basin[x][y] < cavern_basin[x][y - 1]) and \
                    (cavern_basin[x][y] < cavern_basin[x][y + 1]):
                minimums.append([x, y])
    return minimums


def find_minimums(cavern_basin: dict) -> list:
    minimums = find_minimums_corners(cavern_basin)
    minimums.extend(find_minimums_edge(cavern_basin))
    minimums.extend(find_minimums_center(cavern_basin))
    return minimums


def find_this_basin(knownbasin: list, origins: list, cavern_basin: dict) -> list:
    newbasin = knownbasin.copy()
    neworigins = []
    for origin in origins:
        adjacentdelta = [[0], [0]]
        if origin[0] > 0:
            adjacentdelta[0].append(-1)
        if origin[0] < max(cavern_basin.keys()):
            adjacentdelta[0].append(1)
        if origin[1] > 0:
            adjacentdelta[1].append(-1)
        if origin[1] < (len(cavern_basin[0]) - 1):
            adjacentdelta[1].append(1)
        for x in adjacentdelta[0]:
            for y in adjacentdelta[1]:
                if (x == 0 and y == 0) or (x != 0 and y != 0):
                    continue
                newxy = [(origin[0] + x), (origin[1] + y)]
                if newxy not in newbasin:
                    if cavern_basin[newxy[0]][newxy[1]] < 9:
                        neworigins.append(newxy)
    if len(neworigins) > 0:
        newbasin.extend(neworigins)
        newbasin = find_this_basin(newbasin, neworigins, cavern_basin)
    return newbasin

def dedup_lists(theselist: list) -> list:
    finallists = []
    for i in theselist:
        seen = []
        for x in i:
            if x not in seen:
                seen.append(x)
        finallists.append(seen)
    return finallists


def find_basins(cavern_minimums: list, cavern_basin: dict) -> list:
    basins = []
    for i in cavern_minimums:
        basins.append(find_this_basin([i], [i], cavern_basin))
    return basins


def get_total(basins: list) -> int:
    basinsizes = []
    total = 1
    for i in basins:
        basinsizes.append(len(i))
    basinsizes.sort()
    basinsizes.reverse()
    for i in range(3):
        total *= basinsizes.pop(0)
    return total


def main(input_file: str) -> None:
    cavern_basin = get_input(input_file)
    cavern_basin = make_basin_grid(cavern_basin)
    cavern_minimums = find_minimums(cavern_basin)
    basins = find_basins(cavern_minimums,cavern_basin)
    basins = dedup_lists(basins)
    print(get_total(basins))
    

main(input_file)