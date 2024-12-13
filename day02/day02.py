from scripts import *
with open(r'day02\input.txt', 'r') as text_file:

    
    line_list = text_file.readlines() #get the list of line

    safety_list = []
    value = 0
    for line in line_list:  #for each line from the list, print the line
    
        linestring = line.split()
        for i in range(0,len(linestring)):
            linestring[i] = int(linestring[i])
        print(linestring)

        
        safe :bool = False 
        if decreasing_tester(linestring) == True or increasing_tester(linestring) == True:
            safe = True
        if safe == True:
            value += 1

    print(value)

    text_file.close() #don't forget to close the file
    


        
