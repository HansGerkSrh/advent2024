"""
Task description: https://adventofcode.com/2024/day/8

"""

import re 
##### File Import ######

with open(r'day08/Input.txt', 'r') as text_file:
   text = text_file.read()
inputlist = text.splitlines() # splits the text into a list with each row as a string 

# sepperates ech row into a list containing every symbol of the row for better indexing 
x = []
for lines in inputlist:
    x.append(list(lines))
inputlist = x     
        
