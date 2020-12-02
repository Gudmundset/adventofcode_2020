#!/usr/bin/python

def policy_password_input():
    """reads in line-separated numbers of an expense report"""
    try:
        with open('2.txt') as f:
            return f.read()
    except:
        return ""

def unofficial_toboggan_policy_password_decider():
    """
    N1-N2 char: password
    Figures out if the password fits the policy earlier in the line
    N1 min, N2 max, char the character
    """
    valid_lines = []
    db = policy_password_input()
    db_list = db.split('\n')
    for line in db_list:
        policy, password = line.split(':')
        iters, char = policy.split(' ')
        min, max = iters.split('-')
        char_appearances = len([l for l in password if l == char])
        if char_appearances <= int(max) and char_appearances >= int(min):
            valid_lines.append(line)
    return valid_lines

def official_toboggan_policy_password_decider():
    """
    N1-N2 char: password
    Figures out if the password fits the policy earlier in the line
    N1 position 1, N2 position 2, char the character
    (no position 0)
    """
    valid_lines = []
    db = policy_password_input()
    db_list = db.split('\n')
    for line in db_list:
        minmem = ""
        policy, password = line.split(':')
        iters, char = policy.split(' ')
        min, max = iters.split('-')
        password_iter = password.lstrip(' ')
        for num, letter in enumerate(password_iter, start=1):
            if str(num) == min:
                if char == letter:
                    if password_iter[int(max) - 1]:
                        if not password_iter[int(max) - 1] == letter:
                            valid_lines.append(line)
                            break
            if str(num) == max:
                if char == letter:
                    if password_iter[int(min) - 1]:
                        if not password_iter[int(min) - 1] == letter:
                            valid_lines.append(line)
                            break
    return valid_lines

if __name__ == "__main__":
    try:
        print(len(official_toboggan_policy_password_decider()))
    except Exception as e:
        print(e)
