#!/usr/bin/python

import re

def part_1_2():
    """docking rules"""
    mem = {}
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
            print(maskoverwrite)
            for mempair in overwrites:
                address = mempair[0]
                num = format(int(mempair[1], 10), '036b')
                print(len(num),int(address))
                print("value:\t", num)
                print("address:\t", num)
                print("mask:\t", mask)
                newnum = ''
                for n,a in enumerate(num):
                    if n in maskoverwrite:
                        newnum += maskoverwrite[n]
                    else:
                        newnum += a
                print("result:\t", newnum)
                mem[address] = newnum
        
        testlist = []
        for k,v in mem.items():
            testlist.append(int(v.lstrip('0'), 2))
        print(sum(testlist))
                

                    
if __name__ == "__main__":
    part_1_2()
