from typing import List
import re

input_file = 'day_8.txt'


def get_input(myfile: str) -> list:
    with open(myfile, 'r') as subfile:
        sublist = [re.sub('\n', '', x) for x in subfile.readlines()]
    subfile.close()
    returnlist = []
    for i in sublist:
        position = 0
        tmplist=[[], []]
        for x in i.split():
            if x == '|':
                position += 1
            else:
                tmplist[position].append(''.join(sorted(x)))
        returnlist.append(tmplist)
    return returnlist


def process_signal(frame: list) -> list:
    numberlist = ['', '', '', '', '', '', '', '', '', '']
    tmplist = []
    # get known numbers
    for i in frame:
        if len(i) == 2:
            numberlist[1] = i
        elif len(i) == 3:
            numberlist[7] = i
        elif len(i) == 4:
            numberlist[4] = i
        elif len(i) == 7:
            numberlist[8] = i
        else:
            tmplist.append(i)
    # find remaining numbers
    for i in tmplist:
        if len(i) == 5:
            # 2, 3, 5
            if len(''.join(set(i).intersection(numberlist[4]))) == 2:
                numberlist[2] = i
            elif len(''.join(set(i).intersection(numberlist[1]))) == 2:
                numberlist[3] = i
            else:
                numberlist[5] = i
        else:
            # 0, 6, 9
            if len(''.join(set(i).intersection(numberlist[1]))) == 1:
                numberlist[6] = i
            elif len(''.join(set(i).intersection(numberlist[4]))) == 3:
                numberlist[0] = i
            else:
                numberlist[9] = i
    return numberlist


def find_readout(numberlist: list, displayvalues: list) -> int:
    counter = 0
    for i in displayvalues:
        counter *= 10
        counter += numberlist.index(i)
    return counter



def process_frame(signal_and_readout: list) -> int:
    total = 0
    for i in signal_and_readout:
        thisframe = process_signal(i[0])
        total += find_readout(thisframe, i[1])
    return total



def main(input_file: str) -> None:
    sevensegments = get_input(input_file)
    print(process_frame(sevensegments))


main(input_file)
