import operator
def determine_numbers(inputnumbers,operator_list):
    ops = {
        0: operator.add, 
        1: operator.mul, 
        2: operator.concat
        }
    result = int(inputnumbers[1])
    i = 1
    while i < len(inputnumbers)-1: 
        if operator_list[i-1] == 2:
            result = ops[operator_list[i-1]](str(result),(inputnumbers[i+1]))  #executes the operator based on the ops Dictonary that gets defined at the start
        else:
            result = ops[operator_list[i-1]](int(result),int(inputnumbers[i+1]))  #executes the operator based on the ops Dictonary that gets defined at the start
        i += 1
    return result


print(determine_numbers([3267,81,40,27],[0,1,2]))


print