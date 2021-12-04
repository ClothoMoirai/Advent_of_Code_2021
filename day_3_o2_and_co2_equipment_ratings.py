from typing import List
from collections import defaultdict, Counter


def defaultvalue() -> list:
    return []


def read_file(myfilename: str) -> list:
    with open(myfilename, 'r') as myfile:
        myconsumption_list = myfile.read().splitlines()
    myfile.close()
    return myconsumption_list


def count_0_1(myreadings_list: list, offset: int) -> dict:
    numbers_dict = defaultdict(defaultvalue)
    for thisreading in myreadings_list:
        numbers_dict[thisreading[offset]].append(thisreading)
    return numbers_dict


def subprocess_readings(myreadings_list: list, offset:int, preference: int) -> str:
    counts01 = count_0_1(myreadings_list, offset)
    offset += 1
    zero_len = len(counts01['0'])
    one_len = len(counts01['1'])
    if zero_len > one_len:
        if preference:
            result_list = counts01['0']
        else:
            result_list = counts01['1']
    elif zero_len < one_len:
        if preference:
            result_list = counts01['1']
        else:
            result_list = counts01['0']
    else:
        if preference:
            result_list = counts01['1']
        else:
            result_list = counts01['0']
    if len(result_list) > 1:
        result = subprocess_readings(result_list, offset, preference)
    else:
        result = result_list[0]
    return result


def process_readings(myreadings_list: list) -> int:
    offset = 0
    counts01 = count_0_1(myreadings_list, offset)
    offset += 1
    if len(counts01['0']) > len(counts01['1']):
        o2 = counts01['0']
        co2 = counts01['1']
    else:
        o2 = counts01['1']
        co2 = counts01['0']
    o2_result = subprocess_readings(o2, offset, 1)
    co2_result = subprocess_readings(co2, offset, 0)
    return [o2_result, co2_result]


def calculate_total(myresult: list) -> int:
    o2 = 0b0
    co2 = 0b0
    for i in range(len(myresult[0])):
        o2 = o2 << 1
        o2 += int(myresult[0][i])
        co2 = co2 << 1
        co2 += int(myresult[1][i])
    return o2 * co2


def main():
    myreadings_list = read_file('day_3.txt')
    myresult = process_readings(myreadings_list)
    print(calculate_total(myresult))

main()