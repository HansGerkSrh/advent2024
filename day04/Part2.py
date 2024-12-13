from scripts_Part2 import *
with open(r'day04\Input.txt', 'r') as text_file:
    
    line_list = text_file.readlines() #get the list of line
    text_file.close()

    print(line_list[0])

    mainlist = []
    for line in line_list:  #for each line from the list, print the line:
        mainlist.append(list(line))
    
output = x_checker(mainlist)
print(output)