from typing import List
from collections import defaultdict, Counter


def defaultvalue() -> list:
    return []


def read_file(myfilename: str) -> list:
    with open(myfilename, 'r') as myfile:
        myconsumption_list = myfile.read().splitlines()
    myfile.close()
    return myconsumption_list


def process_readings(myreadings_list: list) -> dict:
    myreadings_dict = defaultdict(defaultvalue)
    for this_reading in myreadings_list:
        for i in range(len(this_reading)):
            myreadings_dict[i].append(this_reading[i])
    return myreadings_dict


def calculate_gamma_epsilon(values_dict: dict) -> int:
    gamma = 0b0
    epsilon = 0b0
    for i in values_dict:
        this_bit = int(Counter(values_dict[i]).most_common(1)[0][0])
        gamma = gamma << 1
        gamma += this_bit
        epsilon = epsilon << 1
        if not this_bit:
            epsilon += 1
    return (gamma * epsilon)


def main():
    myreadings_list = read_file('day_3.txt')
    myreadings_dict = process_readings(myreadings_list)
    mypower = calculate_gamma_epsilon(myreadings_dict)
    print(mypower)

main()
