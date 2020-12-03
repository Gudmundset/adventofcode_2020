#!/usr/bin/python

from collections import Counter

def toboggan_ride_input():
    """reads in line-separated numbers of an expense report"""
    try:
        with open('3.txt') as f:
            return f.read()
    except:
        return ""

def main():
    #linematrix = []
    pathmap = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    pathright, pathdown = 0, 0 #starting coordinates
    charfield = '.'
    chartree = '#'
    charmiss = 'O'
    charhit = 'X'

    for p in range(len(pathmap)):
        linematrix = []
        twodown = False
        path = pathmap[p]
        pathright, pathdown = 1, 0
        landscape = toboggan_ride_input()
        landscape = landscape.split('\n')
        if path[1] == 2:
            twodown = True
        for lineno, line in enumerate(landscape):
            record = True
            if twodown:
                if not lineno % 2 == 0:
                    record = False
            line = line*150 #render the whole table lol
            hitdown = False
            hitright = False
            lineresult = []
            for position, plot in enumerate(line, start=1):
                if pathright % path[0] == 0:
                    hitright = True
                if pathdown % path[1] == 0:
                    hitdown = True
                if record and hitright and hitdown and not pathdown == 0:
                    if position == pathright + 1:
                        if plot == charfield:
                            lineresult.append(charmiss)
                            hitright, hitdown = False, False
                            continue
                        if plot == chartree:
                            lineresult.append(charhit)
                            hitright, hitdown = False, False
                            continue
                lineresult.append(plot)
            #print(''.join(lineresult),pathright,pathdown)
            linematrix += lineresult
            if twodown:
                if record:
                    pathright += path[0]
            else:
                pathright += path[0]
            pathdown += path[1]
        xcount = Counter()
        for linem in linematrix:
            if charhit in linem:
                xcount[charhit] += 1
        print(path, xcount)
        

if __name__ == "__main__":
    main()
