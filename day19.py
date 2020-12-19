#!/usr/bin/python

import yaml


def opt_parser(input, rules):
  
  attempt = rules[input]
  if attempt == 'a' or attempt == 'b':
    return attempt
  else:
    opt = False
    rulestring = ""
    optrulestring = ""
    for r in attempt.split(' '):
      if r == '|':
        opt = True
        continue
      attempt2 = opt_parser(int(r), rules)
      if isinstance(attempt2, str):
        rulestring += attempt2
      if isinstance(attempt2, tuple):
        roi, opti = attempt2
        rulestring += roi
        optrulestring += opti
      if opt and r.isnumeric():
        optrulestring += rules[int(r)]
    return rulestring, optrulestring
  


def part_1_2():
  """monster messages"""
  with open('19test.yaml') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
  input = data['input'].split(' ')
  rules = {k:v for k,v in data.items() if k != 'input'}

  for key, rule in rules.items():
    opt = False
    rulestring = ""
    optrulestring = ""
    for r in rule.split(' '):
      if r == '|':
        opt = True
        continue
      if r.isnumeric() and not opt:
        attempt = opt_parser(int(r), rules)
        if isinstance(attempt, str):
          rulestring += attempt
        if isinstance(attempt, tuple):
          roi, opti = attempt
          rulestring += roi
          optrulestring += opti
      if opt and r.isnumeric():
        optrulestring += rules[int(r)]
    print(rulestring, optrulestring)

  for i in input:
    pass
        
          
if __name__ == "__main__":
    part_1_2()
    
