import re

with open(r'day03\input.txt', 'r') as text_file:

    file_content = text_file.read()
    text_file.close() #don't forget to close the file

    list_return = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",file_content)
    return_value = 0
    i = 0
    while i < len(list_return):
        return_value += (int(list_return[i][0])) * int((list_return[i][1]))
        i += 1



    import re

