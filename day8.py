#!/usr/bin/python

import sys
import time

from collections import Counter

def acc_jump(initial, num):
    op, num = num[0], int(num[1:])
    if op == '+':
        return int(initial + num)
    if op == '-':
        return int(initial - num)


def part_1_2():
    """find pattern in dict of lists"""
    with open('8.txt') as f:
        f = f.read().split('\n')
        infinite_loop_not_detected = True
        try:
            history = Counter()
            inst_hist = []
            accumulator = 0
            nextpos = 0
            while infinite_loop_not_detected:
                for no, instruction in enumerate(f, start=1):
                    if nextpos:
                        if no == nextpos:
                            nextpos = 0
                        else:
                            continue
                    code, num = instruction.split(' ')
                    hist = '{0}{1}'.format(no, instruction)
                    inst_hist.append(instruction)
                    print(hist)
                    if not history[hist]:
                        history[hist] += 1
                    else:
                        print('final', accumulator, hist)
                        print(inst_hist[::-1])
                        infinite_loop_not_detected = False
                        break
                    if code == 'nop':
                        continue
                    if code == 'acc': 
                        accumulator = acc_jump(accumulator, num)
                    if code == 'jmp':
                        nextpos = acc_jump(no, num)
                        break
                print(accumulator)
                time.sleep(.1)
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    part_1_2()
    #for part 2, replaced all jmps going backwards by hand in input to get answer. 
    # The answer for my input was changing jmp to nop for #322.
    
