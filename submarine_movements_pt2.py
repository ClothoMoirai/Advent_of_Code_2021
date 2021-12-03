from typing import List
import re


def compute_moves(movements_list: list):
    position = [ 0, 0, 0] # horizontal, vertical, aim
    for this_movement in movements_list:
        movement = this_movement.split()
        movement[1] = int(re.sub('[\D]','',movement[1]))
        if movement[0].casefold() == 'forward':
            position[0] += movement[1]
            if position[2] > 0:
                position[1] += position[2] * movement[1]
        elif movement[0].casefold() == 'down':
            position[2] += movement[1]
        elif movement[0].casefold() == 'up':
            position[2] -= movement[1]
        else:
            print("unknown movement:", movement)
    return position


def get_moves(movement_filename: str) -> list:
    with open(movement_filename, 'r') as movements_file:
        movements_list = movements_file.readlines()
    return movements_list


def main():
    movement_filename = 'movements.txt'
    movements_list = get_moves(movement_filename)
    position = compute_moves(movements_list)
    print((position[0] * position[1]))

main()