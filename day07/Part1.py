from scripts_Part1 import *
import re

##### File Import ######

with open(r'day07/Input.txt', 'r') as text_file:
    
    inputlist = text_file.read().splitlines()
    text_file.close()

inputlist_transformed = []

i = 0
while i < len(inputlist):    
    x = re.split(":|(?<=\d)\s", inputlist[i]) #Regex that Splits each Line From the Input  text when either theres a ":" or a whitespace after a number
    inputlist_transformed.append(x)
    #print(inputlist_transformed[i])
    i += 1


def permutation_generator(operator_amount, dimension):
    if operator_amount == 0:
        return [[]]
    smaller = permutation_generator(operator_amount- 1, dimension)
    result = []
    for i in smaller:
        for digit in range(dimension):
            result.append(i + [digit])
    return result
    
print(permutation_generator(4,2))


def check_testvalue(inputlist_transformed,dimension):
    i = 1
    operator_amount = (len(inputlist_transformed)-2) #how many operators are going to be used
    while i < (2^operator_amount): #possible different permutations of the arrangement of the opperators   
        if inputlist_transformed[0] == num:
            return True


resultsum = 0
j = 0
while j < len(inputlist_transformed):
    if check_testvalue(inputlist_transformed) == True: #chekcs if teh current Line is a Valid equation according to the challange rules
        resultsum += int(inputlist_transformed[j][0]) #if true adds the test Value to the result 
    j += 1

print(resultsum)


