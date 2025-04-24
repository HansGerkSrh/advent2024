#from scripts_Part1 import *
import re

##### File Import ######

with open(r'day08/Input.txt', 'r') as text_file:
   text = text_file.read()
unique_chars = ''.join(sorted(set(re.findall(r'[a-zA-Z0-9]', text)))) # find every unique existing char in the whole text and return it as a string 
inputlist = text.splitlines() # splits the text into a list with each row as a string 
del text

# sepperates ech row into a list containing every symbol of the row for better indexing 
x = []
for lines in inputlist:
    x.append(list(lines))
inputlist = x     
        
# von jedem char alle Instanzen finden
# zu jeder instanz alle relativen koordinaten zu den jeweils anderen punkten des selben Chars ermitteln 
# antinode koordinaten errechnen 


##### initialise dict. and add coordinate entrys #####

coordinatelist = {} # initialise dict.
columnlenght = len(inputlist) # define lenght of y axis
rowlenght = len(inputlist[0]) # define lenght of x axis

for char in unique_chars: # itterate for every char 
    column = 0
    coordinatelist[str(char)] = [] # defines empty list for each char 
    while column < columnlenght: 
        row = 0
        while row < rowlenght:
            if char == inputlist[column][row]: # checks every row and every column, of the input list, is true if its the current char 
                # appends a dictonary of the coordinates of each char to the coordinatelist entry of that char, also initialise "relative_position" list
                coordinatelist[str(char)].append({"coordinate":{"x": row , "y": column},"relative_positions": []}) 
            row += 1
        column += 1

##### calculate relative positions #####

# loop for every character Entry 
for i in coordinatelist: 
    # loops through every coordinate and calculates its relative location to every other one
    for first_coordinatenumber in range(len(coordinatelist[i])):
        for coordinatenumber in range(len(coordinatelist[i])):
            # only subtractes if its not the same coordinate
            if (
                coordinatelist[i][coordinatenumber]["coordinate"]["x"] != coordinatelist[i][first_coordinatenumber]["coordinate"]["x"]
                ) and (
                coordinatelist[i][coordinatenumber]["coordinate"]["y"] != coordinatelist[i][first_coordinatenumber]["coordinate"]["y"]
                ):
                    # appends a new dictionary with the corresponding x and y value to the "relative_positions" entry of each coordinate
                    coordinatelist[i][coordinatenumber]["relative_positions"].append(
                        {
                        # entry for the x Value
                        "x":(coordinatelist[i][first_coordinatenumber]["coordinate"]["x"] - coordinatelist[i][coordinatenumber]["coordinate"]["x"]),
                        # entry for the y Value
                        "y": (coordinatelist[i][first_coordinatenumber]["coordinate"]["y"] - coordinatelist[i][coordinatenumber]["coordinate"]["y"])
                        })
                    
##### calculating antinode values ######
result_set = set()
for i in coordinatelist: 
    for coordinatenumber in range(len(coordinatelist[i])):
        for relative_position_number in range(len(coordinatelist[i][coordinatenumber]["relative_positions"])):
            coordinates = [0,0]
            coordinates[0] = (coordinatelist[i][coordinatenumber]["coordinate"]["x"] -
                              coordinatelist[i][coordinatenumber]["relative_positions"][relative_position_number]["x"])
            coordinates[1] = (coordinatelist[i][coordinatenumber]["coordinate"]["y"] -
                              coordinatelist[i][coordinatenumber]["relative_positions"][relative_position_number]["y"])
            result_set.add(tuple(coordinates))

#print(result_set)

##### sorting out impossible positions #####

result_set = (list(result_set))
#print(len(result_set))
filtered_list = []

max_x = rowlenght # maximum possible x Value
max_y = columnlenght # maximum possible y Value

for i in range(len(result_set)): # itterate over each coordinate in the list and check if its withon the boundaries of the map 
    if ((result_set[i][0] >= 0 and result_set[i][0] < max_x) and (result_set[i][1] >= 0 and result_set[i][1] < max_y)):
        filtered_list.append(result_set[i]) #if its within the map, append the value to the finale filtered list

print(len(filtered_list)) # prints the result value (awnser to the puzzle)

##### debugging ##### 

# for line in inputlist:
#     print(line)
# print(unique_chars)

# for i in coordinatelist:
#     print(i)
#     for coordinatenumber in range(len(coordinatelist[i])):
#         print(coordinatelist[i][coordinatenumber])

# for i in coordinatelist: 
#     print(i)
#     for coordinatenumber in range(len(coordinatelist[i])):
#         print(coordinatelist[i][coordinatenumber]["relative_positions"])
