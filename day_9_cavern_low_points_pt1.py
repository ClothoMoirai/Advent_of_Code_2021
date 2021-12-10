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
            minimums.append(cavern_basin[i[0]][i[1]])
    return minimums


def find_minimums_edge(cavern_basin: dict) -> list:
    minimums = []
    maxrow = max(cavern_basin.keys())
    maxcolumn = len(cavern_basin[0]) - 1
    for i in range(1,maxcolumn):
        if (cavern_basin[0][i] < cavern_basin[0][i - 1]) and \
                (cavern_basin[0][i] < cavern_basin[0][i + 1]) and \
                (cavern_basin[0][i] < cavern_basin[1][i]):
            minimums.append(cavern_basin[0][i])
        if (cavern_basin[maxrow][i] < cavern_basin[maxrow][i - 1]) and \
                (cavern_basin[maxrow][i] < cavern_basin[maxrow][i + 1]) and \
                (cavern_basin[maxrow][i] < cavern_basin[maxrow - 1][i]):
            minimums.append(cavern_basin[maxrow][i])
    for i in range(1,maxrow):
        if (cavern_basin[i][0] < cavern_basin[i - 1][0]) and \
                (cavern_basin[i][0] < cavern_basin[i + 1][0]) and \
                (cavern_basin[i][0] < cavern_basin[i][1]):
            minimums.append(cavern_basin[i][0])
        if (cavern_basin[i][maxcolumn] < cavern_basin[i - 1][maxcolumn]) and \
                (cavern_basin[i][maxcolumn] < cavern_basin[i + 1][maxcolumn]) and \
                (cavern_basin[i][maxcolumn] < cavern_basin[i][maxcolumn - 1]):
            minimums.append(cavern_basin[i][maxcolumn])
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
                minimums.append(cavern_basin[x][y])
    return minimums


def find_minimums(cavern_basin: dict) -> list:
    minimums = find_minimums_corners(cavern_basin)
    minimums.extend(find_minimums_edge(cavern_basin))
    minimums.extend(find_minimums_center(cavern_basin))
    return minimums


def main(input_file: str) -> None:
    cavern_basin = get_input(input_file)
    cavern_basin = make_basin_grid(cavern_basin)
    cavern_minimums = find_minimums(cavern_basin)
    print(sum(cavern_minimums) + len(cavern_minimums))


main(input_file)