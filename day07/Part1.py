#from scripts_Part1 import *
import operator
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


def determine_numbers(inputnumbers,operator_list,ops): #function that gets a set of numbers and a set of operators and returns the reult of the calculation
    
    result = int(inputnumbers[1]) #variable to add each operation reslut onto, starts with first number (0 is the test number)
    i = 1
    while i < len(inputnumbers)-1: 
        result = ops[operator_list[i-1]](result,int(inputnumbers[i+1]))  #executes the operator based on the ops Dictonary that gets defined at the start
        i += 1
    return result


def check_testvalue(inputnumbers,dimension,ops):
    i = 0
    operator_amount = (len(inputnumbers)-2) #how many operators are going to be used
    operator_permutations = permutation_generator(operator_amount,dimension)
    while i < len(operator_permutations): #possible different permutations of the arrangement of the opperators   
        if int(inputnumbers[0]) == determine_numbers(inputnumbers,operator_permutations[i],ops): 
            return True
        i += 1
    return False

#define the operator alias to use the generated permuation values as operators
ops = {   
        0: operator.add, 
        1: operator.mul
        }

dimension = len(ops)

resultsum = 0
j = 0
while j < len(inputlist_transformed):
    if check_testvalue(inputlist_transformed[j],dimension,ops) == True: #checks if the current Line is a Valid equation according to the challange rules
        resultsum += int(inputlist_transformed[j][0]) #if true adds the test Value to the result 
    j += 1

print(resultsum)




