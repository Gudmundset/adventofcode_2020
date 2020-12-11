#!/usr/bin/python

import copy
import time
from collections import Counter

def check_visibility(row,column,rows,columns,newgrid):
    results = []
    rows = rows + 1
    columns = columns + 1
    for y in range(max(column - 1, 0), min(column + 2, columns)):
        for x in range(max(row - 1, 0), min(column + 2, rows)):
            if y != column or x != row:
                dx, dy = x - row, y - column
                d = 1
                while column + d * dy in range(columns) and row + d * dx in range(rows):
                    try:
                        if newgrid[column + d * dy][column + d * dx] is False:
                            d += 1
                        else:
                            results.append(newgrid[column + d * dy][row + d * dx])
                            break
                    except: break
    return results

def check_neighbour(check_row,check_column,rows,columns):
    #how deep the search is:
    search_min = -1
    search_max = 2
    #empty list to append neighbours into.
    neighbour_list = []
    for row in range(search_min,search_max):
        for column in range(search_min,search_max):
            neighbour_row = check_row + row
            neighbour_column = check_column + column 
            valid_neighbour = True
            if (neighbour_row) == check_row and (neighbour_column) == check_column:
                valid_neighbour = False
            if (neighbour_row) < 0 or (neighbour_row) >= rows:
                valid_neighbour = False
            if (neighbour_column) < 0 or (neighbour_column) >= columns:
                valid_neighbour = False
            if valid_neighbour:
                neighbour_list.append((neighbour_row,neighbour_column))
    return neighbour_list  

def main_loop(newgrid,fulllength,floor,empty,occupied,part2=False):
    
    newgrid2 = copy.deepcopy(newgrid)
    print('-')
    for no1, row in enumerate(newgrid):
        for no2, seat in enumerate(row):
            newgrid2[no1][no2] = seat
            adj = check_neighbour(no1,no2,fulllength,len(row))
            if part2:
                visibility = check_visibility(no1,no2,fulllength,len(row),newgrid)
            if seat == floor: #nobody sits on the floor
                continue
            if seat == empty:
                check_empty = []
                if part2:
                    for v in visibility:
                        for r in v:
                            if r == occupied:
                                check_empty.append(r)
                                break
                            if r == empty:
                                check_empty.append(r)
                                break
                for a in adj:
                    check_empty.append(newgrid[a[0]][a[1]])
                any_occ = False
                for c in check_empty:
                    if c == occupied:
                        any_occ = True
                        break
                if not any_occ:
                    newgrid2[no1][no2] = occupied
            if seat == occupied:
                check_occupied = []
                if part2:
                    for v in visibility:
                        for r in v:
                            if r == occupied:
                                check_occupied.append(r)
                                break
                            if r == empty:
                                check_occupied.append(r)
                                break
                for b in adj:
                    check_occupied.append(newgrid[b[0]][b[1]])
                if len([o for o in check_occupied if o == occupied]) >= 5:    
                    newgrid2[no1][no2] = empty
        
    return newgrid2    

def part_1_2():
    """seat rules"""
    empty = 'L'
    floor = '.'
    occupied = '#'
    rounds = 99
    part2 = True
    
    with open('11.txt') as full:
        full = full.readlines()
        full = [(list(line.replace('\n',''))) for line in full]
        fulllength = len(full)
        newgrid = full
        for round in range(0,rounds):
            x_count = Counter()
            newgrid2 = copy.deepcopy(newgrid)
            newgrid = main_loop(newgrid2,fulllength,floor,empty,occupied,part2=part2)
            for line in newgrid:
                x_count[occupied] += len([x for x in line if x == occupied])
                print(''.join(line))
            # time.sleep(.01)
            print(x_count)

                        
if __name__ == "__main__":
    part_1_2()
