#!/usr/bin/python

import re
from itertools import combinations


def gen_mask_multiplicity(mask_combo, address, length):
    new_addressdict = {}
    address = list(address)
    for combo in mask_combo.keys():
        new_addressdict[combo] = (0,1)
    for add,com in new_addressdict.items():
        for c in com:
            address[add] = str(c)
            if not 'X' in address:
                yield ''.join(address)

def part_1_2():
    """docking rules"""
    mem = {}
    mem_part2 = {}
    mem_re = r'mem\[(?P<mem>\d+)\] = (?P<num>\d+)'
    maskdict = {}
    memlist = []
    with open('14.txt') as full:
        full = full.readlines()
        full = [line.replace('\n','') for line in full]
        mask = ''
        for line in full:
            if 'mask' in line:
                memlist = []
                mask = line.split('mask = ')[1]
                maskdict[mask] = []
            if 'mem' in line:
                memsearch = re.match(mem_re, line)
                memlist = maskdict[mask]
                memlist.append(memsearch.groups())

        for mask,overwrites in maskdict.items():
            maskoverwrite = {n:o for n,o in reversed(list(enumerate(mask))) if o == '1' or o == '0'}
            part2_maskoverwrite = {n:o for n,o in reversed(list(enumerate(mask))) if o != '0'}
            for mempair in overwrites:
                address = mempair[0]
                num = format(int(mempair[1], 10), '036b')
                address_num = format(int(address, 10), '036b')
                print('--')
                print("part1\nvalue:\t\t", num)
                print("mask:\t\t", mask)
                newnum = ''
                for n,a in enumerate(num):
                    if n in maskoverwrite:
                        newnum += maskoverwrite[n]
                    else:
                        newnum += a
                newaddress = ''
                for n2,a2 in enumerate(address_num):
                    if n2 in part2_maskoverwrite:
                        newaddress += part2_maskoverwrite[n2]
                    else:
                        newaddress += a2
                print("result:\t\t", newnum)
                print("part2\naddress:\t", address_num)
                print("mask:\t\t", mask)
                print("result:\t\t", newaddress)
                print(part2_maskoverwrite)
                mem[address] = newnum

                part2_maskcombo = {n:o for n,o in reversed(list(enumerate(mask))) if o == 'X'}
                newadds = []
                for x in range(len(part2_maskcombo.keys())):
                    for gen in gen_mask_multiplicity(part2_maskcombo, newaddress, len(part2_maskcombo.keys())):
                        newadds.append(gen)
                print(newadds)
                for add in newadds:
                    mem_part2[add] = num
        
        testlist = []
        for k,v in mem.items():
            testlist.append(int(v.lstrip('0'), 2))
        print(sum(testlist))
        testlist = []
        for k,v in mem_part2.items():
            testlist.append(int(v.lstrip('0'), 2))
        print(sum(testlist))
                

                    
if __name__ == "__main__":
    part_1_2()
    
