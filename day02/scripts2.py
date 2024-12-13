from scripts import *

def combination_mixer(linestring):
    linestring_return = [linestring]
    k = 0
    while k < len(linestring):
        i = 0
        x =[]
        while i < len(linestring):
            if k != i:
                x.append(linestring[i])
            i += 1
        linestring_return.append(x)   
        k += 1
    return linestring_return

def decreasing_tester_combinaions(linestring):
    k = 0
    while k < len(linestring):
        if decreasing_tester(linestring[k]) == True:
            return True
        k += 1
    return False

def increasing_tester_combinations(linestring):
    k = 0
    while k < len(linestring):
        if increasing_tester(linestring[k]) == True:
            return True
        k += 1
    return False