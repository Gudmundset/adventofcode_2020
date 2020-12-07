#!/usr/bin/python

import re
from collections import Counter

def bag_rule_input():
    """reads in line-separated numbers of an customs survey input"""
    with open('7.txt') as f:
        return f.read()

def remove_num(bag):
    return bag[2:]

SHINY_GOLD_BAG_COUNTER = 0

def recursive_bag(pattern, contents, rule_dict, count=1, nested_counting=False,power=1):
    """find pattern in dict of lists"""
    #print("recursing", count, contents)
    bagmap = {}
    if nested_counting:
        #print("recursing", count)
        bags_this_level = sum([int(t[:2]) for t in contents])
        bagmap = {remove_num(t):int(t[:2]) for t in contents}
        if bagmap:
            #print(bagmap, "power:", power)
            global SHINY_GOLD_BAG_COUNTER
            SHINY_GOLD_BAG_COUNTER += bags_this_level * power * count
            #print(bags_this_level*power*count)
        #print(contents, "bags this level: ", bags_this_level)
    bags = [remove_num(t) for t in contents]
    bagsearch = [b for b in bags if pattern == b]
    if bagsearch:
        return True
    else:
        for bag in bags:
            #print('searching', bag, rule_dict[bag], count)
            if bag in bagmap:
                power = bagmap[bag]
            else:
                power = 0
            test = recursive_bag(pattern, rule_dict[bag], rule_dict, count=count+1, nested_counting=nested_counting,power=power*count)
            if test:
                return True

def part_1_and_2():
    rule_dict = {}
    bag_counter = Counter()

    pattern = "shiny gold"
    rule = r"(?P<parent>.*) bags contain (?P<child>.*)"
    rule2 = "([0-9]+ \w+ \w+)"
    bag_rules = bag_rule_input().split('\n')
    for bags in bag_rules:
        search = re.search(rule, bags)
        parent, child = search.groups()
        if child:
            rule_dict[parent] = re.findall(rule2, child)
    for bag, contents in rule_dict.items():
        #print('--',bag,contents)
        if bag == "shiny gold":
            looking = recursive_bag(pattern, contents, rule_dict, nested_counting=True)
            
        else:
            looking = recursive_bag(pattern, contents, rule_dict)
        if looking:
            bag_counter[bag] += 1
    #print(bag_counter)
    print("part 1: ", sum(bag_counter.values()))
    global SHINY_GOLD_BAG_COUNTER
    print("part 2: ", SHINY_GOLD_BAG_COUNTER)


if __name__ == "__main__":
    part_1_and_2()
