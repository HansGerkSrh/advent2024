from scripts_Part1 import *
import re
with open(r'day05\Input.txt', 'r') as text_file:
    
    ordering_rules_input_array = text_file.read().splitlines()
    text_file.close()
    
i = 0
while i < len(ordering_rules_input_array):
    linelist = re.split(r"\|",ordering_rules_input_array[i])
    ordering_rules_input_array[i] = linelist
    i += 1
    
# for i in range(0,len(ordering_rules_input_array)):
#     print(str(ordering_rules_input_array[i]))

    

with open(r'day05\Input2.txt', 'r') as text_file:
    
    page_num_input_array = text_file.read().splitlines()
    text_file.close()
    
i = 0
while i < len(page_num_input_array):
    linelist = re.split(r",",page_num_input_array[i])
    page_num_input_array[i] = linelist
    i += 1

# for i in range(0,len(page_num_input_array)):
#     print(str(page_num_input_array[i]))

i = 0
full_printorder = []
while i < len(page_num_input_array):
    current_list = []

    current_list = get_relevant_list(ordering_rules_input_array,page_num_input_array[i])

    #print(f'Nr. {i} : {current_list} \n')

    # print(findNumOne(current_list))
    
    printorder = []
    while len(current_list) > 1:

        excluding_num = findNumOne(current_list)
        printorder.append(excluding_num)
        current_list = del_excluded_num(current_list,excluding_num)

        # print(current_list)
        # print(printorder)

    printorder.append(current_list[0][0])
    printorder.append(current_list[0][1])
    # print(printorder)
    full_printorder.append(printorder)
    i += 1



calculating_list = []
i = 0
while i < len(full_printorder):
    if full_printorder[i] == page_num_input_array[i]:
        calculating_list.append(full_printorder[i])
    i += 1

sum = 0
i = 0



while i < len(calculating_list):
    sum += int(calculating_list[i][len(calculating_list[i])//2])
    i+= 1

print(sum)