#!/usr/bin/python

#Not complete at all, but I can't grasp this one yet. I can't do 3D signal processing.

import numpy as np
from scipy.signal import convolve2d

def apply_conways_game_of_life_rules(status):
    live_neighbors = count_live_neighbors(status)
    survive_underpopulation = live_neighbors >= 2
    survive_overpopulation = live_neighbors <= 3
    survive = status * survive_underpopulation * survive_overpopulation
    new_status = np.where(live_neighbors==3, True, survive)  # Reproduce
    new_neighbors = count_live_neighbors(new_status)
    return new_status, new_neighbors 

def count_live_neighbors(status):
    """Counts the number of neighboring live cells"""
    kernel = np.array(
        [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]
    )
    c = convolve2d(status, kernel, mode='same', boundary="fill")
    return c

def part_1_2():
  inactive = '.'
  active = '#'
  with open('17test.txt') as f:
    data = f.readlines()
    data = [list(d.replace('\n','').replace(active, '1').replace(inactive, '0')) for d in data]
  starting_grid = np.array(data).astype(np.int)
  print(starting_grid)
  print(apply_conways_game_of_life_rules(starting_grid))

if __name__ == "__main__":
  part_1_2()
