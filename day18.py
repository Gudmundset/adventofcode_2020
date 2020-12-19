#!/usr/bin/python

import re

def read_file(filename):
    with open(filename) as f:
        return f.readlines()

def _(expression_list):
    if isinstance(expression_list, str):
        return eval(''.join(expression_list))
    else:
        return expression_list


def part_1_2():
    """math bs"""

    regx = r'\(.*?\)'
    #data = read_file('18.txt')
    teststring = "1 + 2 * 3 + 4 * 5 + 6" #71
    teststring2 = "1 + (2 * 3) + (4 * (5 + 6))" #51
    teststring3 = "2 * 3 + (4 * 5)" #26
    teststring4 = "5 + (8 * 3 + 9 + 3 * 4 * 3)" #437
    teststring5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    teststring6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    the_string = teststring4
    # the_string = the_string.replace('(','_(')
    brackets = re.findall(regx, the_string)
    for b in brackets:
        the_string = the_string.replace(b,'')
        the_string += str(_(b))
    expressions = [str(t) for t in the_string.split(' ')]
    working_math = ""
    for n,e in enumerate(expressions,start=1):
        try:
            attempt = _(working_math)
            if attempt:
                working_math = str(attempt)
        except SyntaxError:
            pass
        working_math += e
        print(n,e,working_math)
    print(_(working_math))
        
          
if __name__ == "__main__":
    part_1_2()
    
