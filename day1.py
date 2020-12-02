#!/usr/bin/python

def expense_report_input():
    """reads in line-separated numbers of an expense report"""
    try:
        with open('1.txt') as f:
            return f.read()
    except:
        return ""

def two_fold_expense():
    """two numbers that add to 2020 multiplied and returned at first notice"""
    expense_report = expense_report_input()
    expense_list = expense_report.split('\n')
    for no, line in enumerate(expense_list):
        for num, expense in enumerate(expense_list):
            if num != no:
                if (int(line) + int(expense)) == 2020:
                    return int(line) * int(expense)

def three_fold_expense():
    """three numbers that add to 2020 multiplied and returned at first notice"""
    expense_report = expense_report_input()
    expense_list = expense_report.split('\n')
    for n1, expense1 in enumerate(expense_list):
        for n2, expense2 in enumerate(expense_list):
            if n2 != n1:
                for n3, expense3 in enumerate(expense_list):
                    if n3 != n1 and n3 != n2:
                        if (int(expense1) + int(expense2)) + int(expense3) == 2020:
                            return int(expense1) * int(expense2) * int(expense3)

if __name__ == "__main__":
    print(two_fold_expense())
    print(three_fold_expense())
        
