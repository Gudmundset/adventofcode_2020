#!/usr/bin/python

from collections import Counter

def customs_input():
    """reads in line-separated numbers of an customs survey input"""
    with open('6.txt') as f:
        return f.read()

def part_1():
    """print number of people who answered yes to which questions"""
    survey = customs_input().split('\n\n')
    total = Counter()
    for s in survey:
        s = s.replace('\n', '')
        s = ''.join((sorted(set(s))))
        for letter in s:
            total[letter] += 1
    print(sum(total.values()))

def part_2():
    """print who answered yes to which questions for everyone in group"""
    survey = customs_input().split('\n\n')
    total = Counter()
    for s in survey:
        people = len(s.split('\n'))
        answer_counter = Counter()
        for person in s:
            for answer in person:
                if answer != '\n':
                    answer_counter[answer] += 1
        answer_total = {k:v for k,v in answer_counter.items() if v == people}
        answer_totals = {k:1 for k,v in answer_total.items()}
        total.update(answer_totals)
    print(sum(total.values()))



if __name__ == "__main__":
    part_1()
    part_2()
