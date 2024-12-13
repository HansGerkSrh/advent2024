from scripts_Part1 import *
with open(r'day04\Input.txt', 'r') as text_file:
    
    line_list = text_file.readlines() #get the list of line
    text_file.close()

    mainlist = []
    for line in line_list:  #for each line from the list, print the line:
        mainlist.append(list(line))
    
output = 0

print(mainlist[0])

print(horizontal_search_l_to_r(mainlist))
output += horizontal_search_l_to_r(mainlist)
print(horizontal_search_r_to_l(mainlist))
output +=horizontal_search_r_to_l(mainlist)
print(vertikal_search_l_to_r(mainlist))
output +=vertikal_search_l_to_r(mainlist)
print(vertikal_search_r_to_l(mainlist))
output +=vertikal_search_r_to_l(mainlist)
print(diagonal_search__down_l_to_r(mainlist))
output +=diagonal_search__down_l_to_r(mainlist)
print(diagonal_search__down_r_to_l(mainlist))
output +=diagonal_search__down_r_to_l(mainlist)
print(diagonal_search__up_l_to_r(mainlist))
output +=diagonal_search__up_l_to_r(mainlist)
print(diagonal_search__up_r_to_l(mainlist))
output +=diagonal_search__up_r_to_l(mainlist)
print(output)