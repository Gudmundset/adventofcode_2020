#!/usr/bin/python

def boarding_input():
    """reads in line-separated numbers of an boarding pass input"""
    with open('5.txt') as f:
        return f.read()

def bsp_decider(iter, inp):
    """determines whether to return upper or lower"""
    length = len(iter)
    middle = length // 2 #floor
    if inp == 'F': return iter[:middle]
    if inp == 'B': return iter[middle:]
    if inp == 'L': return iter[:middle]
    if inp == 'R': return iter[middle:]

def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))

def main():
    """what is the highest seat ID on a boarding pass"""
    """ BINARY SPACE PARTITIONING"""
    h_list = []
    seats = boarding_input().split('\n')
    for seat in seats:
        rows = list(range(0,128))
        cols = list(range(0,8))
        row_input = seat[:7]
        col_input = seat[7:]
        for row in row_input:
            rows[:] = bsp_decider(rows, row)
        row_result = rows
        for col in col_input:
            cols[:] = bsp_decider(cols, col)
        col_result = cols
        seat_id = (row_result[0] * 8) + col_result[0]
        print(seat, row_result, col_result, seat_id)
        h_list.append(seat_id)
    seat_list = sorted(h_list)
    missing = missing_elements(seat_list) #assuming sorted input



if __name__ == "__main__":
    main()
