"""
Task description: https://adventofcode.com/2024/day/8

"""

import re 


def generate_file_data(inputlist):
    """
    Turns original Input like:
    2333133121414131402
    into the File we need 
    00...111...2...333.44.5555.6666.777.888899
    and retuns it as a list of each digit
    """

    resultlist = []
    i = 0
    charindex = 0
    for chars in inputlist:
        if i % 2 == 0:
            #verarbeitung Files
            for gapsize in range(int(chars)):
                resultlist.append(charindex)
            charindex += 1
        else:
            #verarbeitung Gaps
            for gapsize in range(int(chars)):
                resultlist.append(None)
        i += 1
    return resultlist
        

# def is_list_sorting_finished(sorted_list):
#     waitfornumber = False
#     for char in sorted_list:
#         if waitfornumber == False and char == ".":
#             waitfornumber = True
#             continue
#         if waitfornumber == True and isinstance(char,int):
#             return False
#     return True
            

def sort_list(result_list):
    """
    Sorts the List according to the challenge specifications
    """
    unsorted_list =  result_list
    sorted_list = unsorted_list
    i = 0
    k = -1
    for char in unsorted_list:
        if i >= len(sorted_list) + k:
            break
        if char == None:  
            needsnumber = True
            while needsnumber:
                if sorted_list[k] is not None:
                    needsnumber = False
                    number = sorted_list[k]
                    sorted_list[k] = None
                else:
                    k -= 1
            sorted_list[i] = number
            #print_list_to_string(sorted_list) #only works with small input string for visual feedback
        i += 1
    return sorted_list

def calc_checksum(sorted_list):
    i = 0 
    checksum = 0
    while i < len(sorted_list):
        if sorted_list[i] is not None:
            checksum += i * sorted_list[i]
            i += 1
        else:
            return checksum
        
def print_list_to_string(listinput):
    printsum = ""
    for i in range(len(listinput)):
        printsum += str(listinput[i])
    print(printsum)


def main():
    ##### File Import ######
    with open(r'day09/Input.txt', 'r') as text_file:
        text = text_file.read()
        inputlist = text

    file_data = generate_file_data(inputlist)
    sorted_list = sort_list(file_data)
    checksum = calc_checksum(sorted_list)

    #print(file_data)
    print(checksum)
main()
