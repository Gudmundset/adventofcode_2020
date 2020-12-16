#!/usr/bin/python

import yaml
from collections import defaultdict

from functools import reduce
import operator

def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def range_decider(rule_input):
    """
    writing out function to handle specific text input
    i.e.
    class: 1-3 or 5-7

    returns list of two range deciders
    """
    first_rule, second_rule = rule_input.split(' or ')
    fs, fe = first_rule.split('-')
    ss, se = second_rule.split('-')
    return range(int(fs),int(fe)+1), range(int(ss),int(se)+1)

def loop_ticket_part_1(ticket_dict, rule_dict):
    # invalid_nums = set()
    invalid_nums = []
    for ticketclass, tickets in ticket_dict.items():
        if isinstance(tickets, list):
            tickets = tickets.split(' ')
            [tickets] = tickets
        else:
            tickets = tickets.split(' ')
        tn = [t.split(',') for t in tickets]
        for t in tn:
          for num in t:
            # print('--')
            hit = False
            num = int(num)
            for c, r in rule_dict.items():
              for rule in r:
                if num in rule:
                  # print('hit', num, rule)
                  hit = True
                else:
                  pass
                  # print('miss', num, rule)
            if not hit:
              invalid_nums.append(num)
    return invalid_nums

def loop_ticket_part_2(ticket_dict, rule_dict, verbose=False):
    # invalid_nums = set()
    valid_tickets = []
    class_dict = defaultdict(set)
    class_dict2 = defaultdict(set)
    part_2 = set()
    for ticketclass, tickets in ticket_dict.items():
        if isinstance(tickets, list):
            tickets = tickets.split(' ')
            [tickets] = tickets
        else:
            tickets = tickets.split(' ')
        tn = [t.split(',') for t in tickets]
        for t in tn:
          for pos, num in enumerate(t):
            hit = False
            num = int(num)
            for c, r in rule_dict.items():
              for rule in r:
                if num in rule:
                  if verbose:
                      if 'departure' in c:
                        part_2.add(num)
                        print('hit', num, rule, c, pos)
                        class_dict2[c].add(pos)
                        hit = True
                  class_dict[c].add(rule)
                else:
                  pass
                  # print('miss', num, rule, )
            if hit:
              valid_tickets.append(t)
    if verbose:
      print(part_2, class_dict2)
      print("part 2: ", reduce(operator.mul, part_2))
    return valid_tickets, class_dict




def part_1_2():
      """ticket translation"""
      rule_dict = {}
      data = read_yaml('16.yaml')
      rules = {k:v for k,v in data.items() if not 'ticket' in k}
      ticket_dict = {k:v for k,v in data.items() if 'ticket' in k}
      your_ticket = {k:v for k,v in data.items() if 'your ticket' == k}
      # print(your_ticket)

      for rule, value in rules.items():
          first_rule, second_rule = range_decider(value)
          rule_dict[rule] = first_rule, second_rule

      result = loop_ticket_part_1(ticket_dict, rule_dict)
      print("part 1: ", sum(result))

      result2, class_result = loop_ticket_part_2(ticket_dict, rule_dict)
      part_2_range = {r:rule for r,rule in class_result.items() if 'departure' in r}
      print(part_2_range)
      result3, class_result2 = loop_ticket_part_2(your_ticket, rule_dict, verbose=True)


        
          
if __name__ == "__main__":
    part_1_2()
