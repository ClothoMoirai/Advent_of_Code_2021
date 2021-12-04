from pprint import pprint
from typing import List
import re

def get_input(myfile: str) -> list:
    with open(myfile, 'r') as bingofile:
        bingo_input = bingofile.read().splitlines()
    bingofile.close()
    return bingo_input


def process_input(bingo_list: list) -> dict:
    bingo_dict = {'cards': {}}
    bingo_dict['called'] = bingo_list[0].split(',')
    card_counter = 0
    row_counter = 0
    bingo_dict['cards'][card_counter] = {'card': {}, 'results': {}}
    for i in range(2, len(bingo_list)):
        if bingo_list[i] == '':
            card_counter += 1
            row_counter = 0
            bingo_dict['cards'][card_counter] = {'card': {}, 'results': {}}
        else:
            bingo_dict['cards'][card_counter]['card'][row_counter] = re.sub('  *', ' ', bingo_list[i].lstrip()).split(' ')
            bingo_dict['cards'][card_counter]['results'][row_counter] = [ 0, 0, 0, 0, 0]
            row_counter += 1
    return bingo_dict


def check_bingo(card: dict) -> int:
    winner = 0
    for i in card['results']:
        column = []
        for row in card['results']:
            column.append(card['results'][row][i])
        if 0 not in column:
            winner = 1
        if 0 not in card['results'][i]:
            winner = 1
    return winner

def process_calls(bingo_dict: dict) -> dict:
    winning_card = ''
    for i in bingo_dict['called']:
        for card in bingo_dict['cards']:
            if card in bingo_dict['non-winners']:
                for row in range(5):
                    if i in bingo_dict['cards'][card]['card'][row]:
                        bingo_dict['cards'][card]['results'][row][bingo_dict['cards'][card]['card'][row].index(i)] = 1
                if check_bingo(bingo_dict['cards'][card]):
                    if len(bingo_dict['non-winners']) > 1:
                        bingo_dict['non-winners'].remove(card)
                    else:
                        winning_card = {'called': i, 'cardnum': card, 'card': bingo_dict['cards'][card]['card'],
                            'results': bingo_dict['cards'][card]['results']}
                        break
        if winning_card:
            break
    return(winning_card)


def compute_total(bingo_dict: dict) -> int:
    total = 0
    for x in bingo_dict['results']:
        for y in range(len(bingo_dict['results'][x])):
            if not bingo_dict['results'][x][y]:
                total += int(bingo_dict['card'][x][y])
    total *= int(bingo_dict['called'])
    return total

def main() -> None:
    bingo_list = get_input('day_4.txt')
    bingo_dict = process_input(bingo_list)
    bingo_dict['non-winners'] = list(bingo_dict['cards'].keys())
    bingo_dict = process_calls(bingo_dict)
    print(compute_total(bingo_dict))
main()

