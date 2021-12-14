from pprint import pprint
from typing import List
from collections import defaultdict
import re

input_file = 'day_12.txt'


def defaultvalue() -> list:
    return []


def get_input(myfile: str) -> list:
    with open(myfile, 'r') as cavesfile:
        cavesinput = cavesfile.read().splitlines()
    cavesfile.close()
    return cavesinput


def process_input(caveslist: list) -> dict:
    caves = defaultdict(defaultvalue)
    connections = [x.split('-') for x in caveslist]
    for connection in connections:
        if connection[1] != 'start':
            caves[connection[0]].append(connection[1])
        if connection[0] != 'start':
            caves[connection[1]].append(connection[0])
    caves.pop('end')
    return caves


def plotroutes(caves: dict, thisroute: list) -> list:
    completedroutes = []
    for i in caves[thisroute[-1]]:
        temproute = thisroute.copy()
        if i == 'end':
            temproute.append(i)
            completedroutes.append(temproute)
            continue
        elif (i.islower() and (i not in thisroute)) or i.isupper():
            temproute.append(i)
            temproutes = plotroutes(caves, temproute)
            for r in temproutes:
                completedroutes.append(r)
    return completedroutes

    return completedroutes


def begin_route(caves: dict) -> list:
    completedroutes = []
    for i in caves['start']:
        thisroute = plotroutes(caves, ['start', i])
        for r in thisroute:
            completedroutes.append(r)
    return completedroutes

def main(input_file: str) -> None:
    caves = get_input(input_file)
    caves = process_input(caves)
    print(len(begin_route(caves)))


main(input_file)