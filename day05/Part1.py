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


x = get_relevant_list(ordering_rules_input_array,page_num_input_array[i])
print(f'Nr. {i} : {x} \n')
  
