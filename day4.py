#!/usr/bin/python

import re

def passport_input():
    """reads in line-separated numbers of an passport input"""
    try:
        with open('4.txt') as f:
            return f.read()
    except:
        return ""

def part_1():
    result_list = []
    #keyname: is_required
    valid_keys = {'byr': True,
                  'iyr': True,
                  'eyr': True,
                  'hgt': True,
                  'hcl': True,
                  'ecl': True,
                  'pid': True,
                  'cid': False, #optional
                 }
    min_compliant = {k:v for k,v in valid_keys.items() if v}
    passports = passport_input()
    passports = (p.replace('\n',' ') for p in passports.split('\n\n'))
    for passport in passports:
        attr_counter = {}
        for p in passport.split(' '):
            keyattempt, valueattempt = p.split(':')
            if keyattempt in valid_keys:
                if valid_keys[keyattempt]:
                    attr_counter[keyattempt] = valueattempt
        results = {key: value for key, value in valid_keys.items() 
                    if key in attr_counter and value}
        if len(results) >= len(min_compliant):
            result_list.append([results,passport])
    
    print(len(result_list))

def byr(inp):
    inp = int(inp)
    if inp >= 1920 and inp <= 2002:
        return inp
def iyr(inp):
    inp = int(inp)
    if inp >= 2010 and inp <= 2020:
        return inp
def eyr(inp):
    inp = int(inp)
    if inp >= 2020 and inp <= 2030:
        return inp
def hgt(inp):
    mea = ''
    num = 0
    if 'cm' in inp:
        mea = 'cm'
        num = int(inp.split(mea)[0])
        if num >= 150 and num <= 193:
            return str(num) + mea
    if 'in' in inp:
        mea = 'in'
        num = int(inp.split(mea)[0])
        if num >= 59 and num <= 76:
            return str(num) + mea
def hcl(inp):
    regx = r'#[0-9a-f]{6}'
    if re.match(regx,inp):
        return inp
def ecl(inp):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if str(inp) in valid_colors:
        return str(inp)
def pid(inp):
    regx = r'[0-9]{9}$'
    if re.match(regx,inp):
        return inp

def part_2():
    result_list = []
    #keyname: func
    valid_keys = {'byr': byr,
                  'iyr': iyr,
                  'eyr': eyr,
                  'hgt': hgt,
                  'hcl': hcl,
                  'ecl': ecl,
                  'pid': pid,
                  'cid': False, #optional
                 }
    min_compliant = {k:v for k,v in valid_keys.items() if v}
    passports = passport_input()
    passports = [p.replace('\n',' ') for p in passports.split('\n\n')]
    for passport in passports:
        attr_counter = {}
        for p in passport.split(' '):
            keyattempt, valueattempt = p.split(':')
            if keyattempt in valid_keys:
                if valid_keys[keyattempt]:
                    func = valid_keys[keyattempt]
                    if func:
                        if func(valueattempt):
                            attr_counter[keyattempt] = valueattempt
        results = {key: value for key, value in valid_keys.items() 
                    if key in attr_counter and value}
        if len(results) >= len(min_compliant):
            result_list.append([results,passport])
    
    print(len(result_list))


if __name__ == "__main__":
    part_1()
    part_2()
