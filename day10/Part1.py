"""
Task description: https://adventofcode.com/2024/day/10

"""

import re 
with open(r'day10/Input.txt', 'r') as text_file:
    text = text_file.read().splitlines()
    inputlist = []
    i = 0
    for list in text:
        inputlist.append([])
        for number in list: 
            inputlist[i].append(number)
        i += 1

    for i in inputlist:
        print(i)