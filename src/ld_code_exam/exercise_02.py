# Write a function that takes as input a filename.
# The function parses the file reading line by line and determines if the line contains a single valid number.
# It should return a list of all the numbers found in the file.
#
#
# Example input file:
# ==========================================
# #This is an input file with some text and numbers
# 10
#   -50
# Some more numbers follow
# 3.1457
# 12  00 47
# 1.25E-7
# -20000
# ==========================================
#
# Above function should return [10, -50, 3.1457, 1.25E-7, -20000]

import os


def solution(file_name):
    if not os.path.isfile(file_name):
        raise Exception("File not found/ File path is wrong")

    numbers = []
    with open(file_name, mode='r') as file:
        line = file.readline()

        while line:
            if is_number(line):
                numbers.append(line.strip())
            line = file.readline()
    return numbers


def is_number(text):
    try:
        parsed_number = float(text.strip())
        return True
    except:
        return False
