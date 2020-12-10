#!/usr/bin/python

import numpy
from collections import Counter

def part_1_2():
    """find joltage"""
    with open('10.txt') as f:
        x = Counter()
        diff = 3
        numlist = [0] + [int(num) for num in sorted(f.readlines(), key=int)]
        numlist += [numlist[-1]+diff]
        for num in numpy.diff(numlist):
          x[str(num)] += 1
        print("part 1: ", x)

        one_gap = []
        previous = 0
        for i,j in zip(numlist,numlist[1:]):
            if j-i == 3:
                one_gap.append(i-previous)
                previous = j
        print("part 2: ", 2**one_gap.count(2) * 4**one_gap.count(3) * 7**one_gap.count(4))      

if __name__ == "__main__":
    part_1_2()
