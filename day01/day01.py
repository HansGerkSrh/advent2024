# Open the file in read mode
from the_textinator import *
with open(r'day01\day01_text.txt', 'r') as text_file:

    
    line_list = text_file.readlines() #get the list of line

    left_list = []
    right_list = []

    for line in line_list:  #for each line from the list, print the line
    
        linestring = line.split()
        
        left_list.append(((int(linestring[0]))))
        right_list.append(((int(linestring[1]))))

    text_file.close() #don't forget to close the file

left_list.sort()
right_list.sort()
value = 0
i = 0
while i < len(left_list):
    
    value += abs(left_list[i]-right_list[i]) 
    
    i += 1

i = 0
value = 0

while i < len(left_list):
    value += left_list[i] * count_doubes(left_list[i],right_list)
    i += 1

print(value)