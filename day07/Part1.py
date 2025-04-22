from scripts_Part1 import *
import re

##### File Import ######

with open(r'day06/Input.txt', 'r') as text_file:
    
    inputlist = text_file.read().splitlines()
    text_file.close()

#Convert each line into a list
for i in range(0,len(inputlist)):
    inputlist[i] = list(inputlist[i])
    print(inputlist[i])





    




