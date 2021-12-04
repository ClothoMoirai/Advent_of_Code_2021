from typing import List
import re


def clean_depths(depths_list_dirty: list) -> list:
    depths_list = []
    for depth in depths_list_dirty:
        depths_list.append(int(re.sub('[\D]', '', depth)))
    return depths_list


def get_depths(depths_filename: str) -> list:
    with open(depths_filename,'r') as depthsfile:
        depths_list = depthsfile.readlines()
    depthsfile.close()
    return clean_depths(depths_list)


def count_increases(depths_list: list) -> int:
    increase_count = 0
    previous_depth = depths_list[0]
    for this_depth in depths_list:
        if previous_depth < this_depth:
            increase_count+=1
        previous_depth = this_depth
    return increase_count


def compute_measurement_windows(depths: list) -> list:
    range_list = []
    for i in range(2, (len(depths))):
        range_list.append((depths[i-2] + depths[i-1] + depths[i]))
    return range_list


def main() -> None:
    depths_list = get_depths('depth_readings.txt')
    print("depth increases:",count_increases(depths_list))
    range_list = compute_measurement_windows(depths_list)
    increases_count = count_increases(range_list)
    print("depth window group increases:", increases_count)
main()
