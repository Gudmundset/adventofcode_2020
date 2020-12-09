#!/usr/bin/python

from collections import deque
from itertools import combinations

def part_2(numlist, target):
    for a in range(len(numlist)):
        for b in range(0, a + 1):
            if sum(numlist[b:a]) == target:
                answer = sorted(numlist[b:a])
                return answer[0] + answer[-1]

def part_1_2():
    """look through list of nums and figure out if previous X don't add together"""
    with open('9.txt') as f:
        part_1 = 0
        f = f.read().split('\n')
        preamble = 25
        how_many_math = 2
        #fixed length queue
        deq = deque(preamble*[0], preamble)
        for num in f:
            num = int(num)
            runme = [d for d in deq if d]
            if not runme:
                deq.appendleft(num)
                continue
            combos = combinations(deq, how_many_math)
            combos = (com for com in combos if com) #deletes zeroes
            validator = [maths for maths in combos if sum(maths) == num]
            if not validator:
                print("part 1, ", num)
                part_1 = num
            deq.appendleft(num)
        print("part 2, ", part_2([int(num) for num in f], part_1))

if __name__ == "__main__":
    part_1_2()
