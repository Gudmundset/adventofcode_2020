#!/usr/bin/python

from collections import Counter

def part_1_2():
    """memory game"""
    mem_dict = Counter()
    # example_input = [0,3,6]
    # example_input = [1,3,2]
    # example_input = [2,1,3]
    # example_input = [1,2,3]
    # example_input = [2,3,1]
    # example_input = [3,2,1]
    # example_input = [3,1,2]
    part_1_2_input = [1,12,0,20,8,16]
    #example_input = [0,3,6]

    the_list = part_1_2_input
    mem_dict = {a:0 for a in the_list}
    memory = []
    firstseen = False
    # rangenum = 2020
    rangenum = 30000000

    for i in range(0,rangenum):
        if i < len(the_list):
            turn = the_list[i]
        else: 
            if not firstseen:
                turn = 0
                mem_dict[turn] = i
                memory.append(turn)
                # print(f"Turn {i+1}: ", turn)
                firstseen = True
                continue
            else:
                turn = memory[-1]
                for num, appearance in enumerate(reversed(list(memory))):
                    if num == 0:
                        continue
                    if turn == appearance:
                        turn = num
                        break
                if not turn in mem_dict:
                    firstseen = False
                mem_dict[turn] = i
        if i == rangenum:
            print(f"Turn {i+1}: ", turn)
        memory.append(turn)
        
          
if __name__ == "__main__":
    part_1_2()
    
