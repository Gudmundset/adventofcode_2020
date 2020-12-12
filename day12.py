#!/usr/bin/python

import numpy
from scipy.spatial.distance import cdist

def matrix_loop(op, start, spaces, rotation=0):
    # posdict = {"0":"N", "1":"E", "2":"S", "3":"W"}
    spaces = int(spaces)
    X,Y = start
    #Part1
    # if op == "L":
    #     rotation = (rotation - spaces // 90) % 4
    # if op == "R":
    #     rotation = (rotation + spaces // 90) % 4
    # if op == "F":
    #     r = posdict[str(rotation)]
    #     X,Y,start,rotation = matrix_loop(r, start, spaces, rotation)
    for i in range(0,spaces+1):
          if op == "S":
              X,Y = start[0], start[1]+i
          if op == "N":
              X,Y = start[0], start[1]-i
          if op == "E":
              X,Y = start[0]+i, start[1]
          if op == "W":
              X,Y = start[0]-i, start[1]
    return (X,Y)

def rotate_waypoint(waypoint, op, spaces):
    X, Y = waypoint
    spaces = int(spaces)
    if op == "L":
        for i in range(0, spaces):
            X, Y = -Y, X
    if op == "R":
        for i in range(0, spaces):
            X, Y = Y, -X
    return (X, Y)

def part_1_2():
    """movement rules"""
    posdict = {"0":"N", "1":"E", "2":"S", "3":"W"}
    startpos = (0,0)
    pos = (0,0) 
    waypoint = (10,-1)
    #rotation = 1 #starts east for part 1
    with open('12.txt') as full:
        full = full.readlines()
        full = [(list(line.replace('\n',''))) for line in full]
        
        for i, position in enumerate(full):
              op, spaces = position[0], ''.join(position[1:])
              print(position)
              X2, Y2 = waypoint
              X, Y = pos
              if op == 'F':
                pos = X2*int(spaces), Y2*int(spaces)
              if op in ['L','R']:
                rotation = (int(spaces) // 90)
                waypoint = rotate_waypoint(waypoint, op, rotation) 
              if op in posdict.values():
                  waypoint = matrix_loop(op,waypoint,spaces)
              print(pos,waypoint)
              # if i == 10:
              #   break
        p_a = numpy.array(startpos)
        p_b = numpy.array(pos)
        p_a = p_a.reshape(1, -1)
        p_b = p_b.reshape(1, -1)
        manhattan_distance = cdist(p_a, p_b, metric='cityblock')
        print("part 2: ", manhattan_distance)
        
                        
if __name__ == "__main__":
    part_1_2()
    
