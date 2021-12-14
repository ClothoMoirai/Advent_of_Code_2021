from pprint import pprint
from typing import List
from collections import defaultdict
import re

input_file = 'day_11.txt'
cycles = 100

def defaultvalue() -> list:
    return []

def get_input(myfile: str) -> list:
    with open(myfile, 'r') as octopusfile:
        octupusinput = octopusfile.read().splitlines()
    octopusfile.close()
    return octupusinput


def process_octopus(octopus_input: list) -> dict:
    octodict = {'flashes': 0, 'grid': defaultdict(defaultvalue)}
    counter = 0
    for i in octopus_input:
        octodict['grid'][counter] = [int(x) for x in list(i)]
        counter += 1
    return octodict


def increment_grid(octodict: dict) -> dict:
    counter = 0
    cordlist = []
    while any(10 in val for val in octodict['grid'].values()):
        thesex = [key for key, value in octodict['grid'].items() if 10 in value]
        for thisx in thesex:
            thesey = [i for i, x in enumerate(octodict['grid'][thisx]) if x > 9]
            for thisy in thesey:
                if thisx == 0:
                    modx = [0, 1]
                elif thisx == max(octodict['grid'].keys()):
                    modx = [-1, 0]
                else:
                    modx = [-1, 0, 1]
                if thisy == 0:
                    mody = [0, 1]
                elif thisy == (len(octodict['grid'][thisx]) - 1):
                    mody = [-1, 0]
                else:
                    mody = [-1, 0, 1]
                for x in modx:
                    for y in mody:
                        if (octodict['grid'][thisx + x][thisy + y] != 10) and (octodict['grid'][thisx + x][thisy + y] != 0):
                            octodict['grid'][thisx + x][thisy + y] += 1
                octodict['grid'][thisx][thisy] = 0
    if any(0 in val for val in octodict['grid'].values()):
        for x in octodict['grid'].keys():
            for y in range(len(octodict['grid'][x])):
                if octodict['grid'][x][y] == 0:
                    octodict['flashes'] += 1


    for x in octodict['grid'].keys():
        flashed = [i for i, n in enumerate(octodict['grid'][x]) if n < 0]
        for y in flashed:
            octodict['grid'][x][y] = 0
    return octodict


def generate_flashes(octodict: dict) -> dict:
    for i in range(cycles):
        for row in octodict['grid'].keys():
            octodict['grid'][row] = [x+1 for x in octodict['grid'][row]]
        if any(10 in val for val in octodict['grid'].values()):
           increment_grid(octodict)
    return octodict



def main(input_file: str) -> None:
    octopus_input = get_input(input_file)
    octopusgrid = process_octopus(octopus_input)
    octopusgrid = generate_flashes(octopusgrid)
    print(octopusgrid['flashes'])



main(input_file)