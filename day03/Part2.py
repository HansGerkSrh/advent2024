import re

with open(r'day03\input.txt', 'r') as text_file:
    file_content = text_file.read()
    text_file.close() #don't forget to close the file

    filterstring = ""
    
    dofilter = re.split(r'do\(\)',file_content)
    i = 0
    while i < len(dofilter):
         
        dontfilter = re.split(r'don\'t\(\)',dofilter[i])
        filterstring += dontfilter[0]
        i += 1

    list_return = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',file_content)

    return_value = 0
    i = 0
    while i < len(list_return):
        return_value += (int(list_return[i][0])) * int((list_return[i][1]))
        i += 1

#Letzter Part
list_return = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",filterstring)
return_value = 0
i = 0
while i < len(list_return):
    return_value += (int(list_return[i][0])) * int((list_return[i][1]))
    i += 1

print(return_value)