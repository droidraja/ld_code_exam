# Problem
# Given a list of numbers, the "mode" is the value that occurs most often. If no number in the list is repeated, then there is no mode for the list.
#
# For example:
# List1  = [1, 5, 2, 6, 2, 3, 3, 2, 8, 2]
# In List1,  mode is value 2 which occurs 4 times.
# List2 = [500, -100, 200, 50, -100, 300, 50, 700, 50, -100, 500] .
# In List2, there are 2 modes i.e., 50 and -100 both of which occur 3 times.
#
# Write a function that takes a list A as input argument and returns a list of mode values.

from collections import defaultdict


def solution(numbers):
    if numbers is None or len(numbers) == 0:
        return list()
    numbers_count = defaultdict(lambda: 0)
    mode_value = 0
    for number in numbers:
        numbers_count[number] += 1
        mode_value = max(numbers_count[number], mode_value)

    mode_numbers = [number for number in numbers_count if numbers_count[number] == mode_value]

    return mode_numbers
