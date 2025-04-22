from scripts_Part1 import *
import re

##### File Import ######

with open(r'day06/Input.txt', 'r') as text_file:
    
    inputlist = text_file.read().splitlines()
    text_file.close()

#Convert each line into a list
for i in range(0,len(inputlist)):
    inputlist[i] = list(inputlist[i])

counter = 1
y = findcursor(inputlist)
x = moveup(y[0],y[1],counter)

while x != None:
    x = moveright(x[0],x[1],x[2])
    if x != None:
        x = movedown(x[0],x[1],x[2])
        if x != None: 
            x = moveleft(x[0],x[1],x[2])
            if x != None: 
                x = moveup(x[0],x[1],x[2])




    




