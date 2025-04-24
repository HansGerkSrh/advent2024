"""
Task description: https://adventofcode.com/2024/day/8 (you need to put in the solution for part 1 first)

in short: 
-Now every point on a line where 2 anennas are, counts as a antinode location 
"""

import re 
##### File Import ######

with open(r'day08/Input.txt', 'r') as text_file:
   text = text_file.read()
unique_chars = ''.join(sorted(set(re.findall(r'[a-zA-Z0-9]', text)))) # find every unique existing char in the whole text and return it as a string 
inputlist = text.splitlines() # splits the text into a list with each row as a string 

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
column_length = len(inputlist) # define length of y axis
row_length = len(inputlist[0]) # define length of x axis

for char in unique_chars: # itterate for every char 
    column = 0
    coordinatelist[str(char)] = [] # defines empty list for each char 
    while column < column_length: 
        row = 0
        while row < row_length:
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
                ) or (
                coordinatelist[i][coordinatenumber]["coordinate"]["y"] != coordinatelist[i][first_coordinatenumber]["coordinate"]["y"]
                ):
                    # appends a new dictionary with the corresponding x and y value to the "relative_positions" entry of each coordinate
                    coordinatelist[i][coordinatenumber]["relative_positions"].append(
                        {
                        # entry for the x Value
                        "x":(coordinatelist[i][first_coordinatenumber]["coordinate"]["x"] - coordinatelist[i][coordinatenumber]["coordinate"]["x"]),
                        # entry for the y Value
                        "y":(coordinatelist[i][first_coordinatenumber]["coordinate"]["y"] - coordinatelist[i][coordinatenumber]["coordinate"]["y"])
                        })
                    
##### calculating antinode values ######
result_set = set()
for i in coordinatelist: 
    for coordinatenumber in range(len(coordinatelist[i])):
        for relative_position_number in range(len(coordinatelist[i][coordinatenumber]["relative_positions"])):
            k = 0
            while True: # added loop that runs as long as the coordinate values are inside the map / removes filtering out wrongs after
                coordinates = [0,0]
                coordinates[0] = (coordinatelist[i][coordinatenumber]["coordinate"]["x"] -
                               k * coordinatelist[i][coordinatenumber]["relative_positions"][relative_position_number]["x"])
                coordinates[1] = (coordinatelist[i][coordinatenumber]["coordinate"]["y"] -
                               k * coordinatelist[i][coordinatenumber]["relative_positions"][relative_position_number]["y"])
                
                
                x_in_bounds = 0 <= coordinates[0] < row_length
                y_in_bounds = 0 <= coordinates[1] < column_length

                if x_in_bounds and y_in_bounds:
                    result_set.add(tuple(coordinates))
                    k += 1
                else:
                    break

#print(result_set)

print(f'The Result is: {len(result_set)} Antinodes') # prints the result value (awnser to the puzzle)

##### debuging ##### 

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