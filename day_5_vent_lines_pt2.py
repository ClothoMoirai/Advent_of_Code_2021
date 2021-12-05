from pprint import pprint
from typing import List
from collections import defaultdict
import re


def defaultvalue() -> list:
    return []


def get_input(myfile: str) -> list:
    with open(myfile, 'r') as ventsfile:
        ventlines_input = ventsfile.read().splitlines()
    ventsfile.close()
    return ventlines_input


def get_max_xy(ventlines: dict) -> dict:
    for thisline in ventlines['lines']:
        for thispoint in thisline:
            if ventlines['max'][0] < thispoint[0]:
                ventlines['max'][0] = thispoint[0]
            if ventlines['max'][1] < thispoint[1]:
                ventlines['max'][1] = thispoint[1]
    return ventlines


def process_ventlines(ventinput: list) -> dict:
    ventlines_processed = {'max': [0,0], 'lines': []}
    for thisline in ventinput:
        ventlines_tmp = []
        for i in re.sub(' ->','',thisline).split():
            ventlines_tmp.append([int(x) for x in i.split(',')])
        ventlines_processed['lines'].append(ventlines_tmp)
    return get_max_xy(ventlines_processed)


def generate_grid(ventlines: dict) -> dict:
    ventlines['grid'] = defaultdict(defaultvalue)
    for x in range(ventlines['max'][0] + 1):
        for y in range(ventlines['max'][1] + 1):
            ventlines['grid'][x].append(0)
    return ventlines


def plotlines(ventlines:dict) -> dict:
    for thisline in ventlines['lines']:
        currentx, currenty = thisline[0]
        targetx, targety = thisline[1]
        if currentx < targetx:
            diffx = 1
            targetx += 1
        elif currentx > targetx:
            diffx = -1
            targetx -= 1
        else:
            diffx = 0
        if currenty < targety:
            diffy = 1
            targety += 1
        elif currenty > targety:
            diffy = -1
            targety -= 1
        else:
            diffy=0
        if diffx and diffy:
            xrange = list(range(currentx, targetx, diffx))
            yrange = list(range(currenty, targety, diffy))
            for i in range(len(xrange)):
                ventlines['grid'][xrange[i]][yrange[i]] += 1
        elif diffx:
            for thisx in range(currentx, targetx, diffx):
                ventlines['grid'][thisx][currenty] += 1
        else:
            for thisy in range(currenty, targety, diffy):
                ventlines['grid'][currentx][thisy] += 1
    return ventlines


def count_overlaps(ventgrid: dict) -> int:
    overlap_count = 0
    for x in ventgrid:
        for y in ventgrid[x]:
            if y > 1:
                overlap_count += 1
    return overlap_count

def main():
    ventlines = get_input('day_5.txt')
    ventlines = process_ventlines(ventlines)
    ventlines = generate_grid(ventlines)
    ventlines = plotlines(ventlines)
    print(count_overlaps(ventlines['grid']))

main()