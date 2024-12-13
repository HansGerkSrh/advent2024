def findNumOne(list_input):
    k = 0
    i = 0

    while i < len(list_input):   
        if list_input[k][0] == list_input[i][1]:
            i = 0
            k += 1
        else:
            i += 1
        
    return(list_input[k])

def check_number(number,wanted_numbers):
    i = 0
    while i < len(wanted_numbers):
        if number == wanted_numbers[i]:
            return True
        else:
            i += 1
    return False


def get_relevant_list(list_input,wanted_numbers):
    i = 0
    sorted_list = []
    while i < len(list_input):
        if check_number(list_input[i][0],wanted_numbers) and check_number(list_input[i][1],wanted_numbers):
            sorted_list.append(list_input[i])
        i += 1
    return sorted_list


