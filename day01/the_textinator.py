def the_digitator(number):
    returnarray = []
    while number > 0:
        returnarray.append(number%10)
        number = number // 10
    return returnarray

def count_doubes(number,array):
    returnnumber = 0
    i = 0
    while i < len(array):
        if number == array[i]:
            returnnumber += 1
        i += 1
    return returnnumber