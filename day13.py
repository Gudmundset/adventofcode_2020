#!/usr/bin/python

import math



def part_1_2():
    """seat rules"""
    earliest_time = []
    busline = []
    maxrange = 9999
    abstol = 99
    
    with open('13.txt') as full:
        full = full.readlines()
        full = [line.replace('\n','') for line in full]
        for line in full:
            if line.isdigit():
                earliest_time.append(line)
            if ',' in line:
                busline.append(line)
        for run in range(0,len(earliest_time)):
            busrange = {}
            earliest = earliest_time[run]
            busses = busline[run].split(',')
            busses = [int(bus) for bus in busses if not bus == 'x']
            for bus in busses:
                bustimes = []
                for b in range(0,maxrange):
                    bustime = bus*b
                    if math.isclose(int(earliest),bustime, abs_tol=abstol):
                        print(bustime, int(earliest), bustime - int(earliest), bus)
                    bustimes.append(int(bus)*b)
                busrange[bus] = bustimes
                        
if __name__ == "__main__":
    part_1_2()
