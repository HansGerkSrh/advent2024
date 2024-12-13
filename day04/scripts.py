def horizontal_search_l_to_r(mainlist):
    return_value = 0

    k = 0
    while k < len(mainlist):
        i = 0
        while i < len(mainlist[k])-3:
            if mainlist[k][i] == "X":
                if mainlist[k][i+1] == "M":
                    if mainlist[k][i+2] == "A":
                        if mainlist[k][i+3] == "S": 
                            return_value += 1 
            i += 1
        k += 1    
    return return_value


def horizontal_search_r_to_l(mainlist):
    return_value = 0

    k = 0
    while k < len(mainlist):
        i = 0
        while i < len(mainlist[k])-3:
            if mainlist[k][i] == "S":
                if mainlist[k][i+1] == "A":
                    if mainlist[k][i+2] == "M":
                        if mainlist[k][i+3] == "X": 
                            return_value += 1 
            i += 1

        k += 1    
    return return_value

def vertikal_search_l_to_r(mainlist):
    return_value = 0

    k = 0
    while k < len(mainlist)-3:
        i = 0
        while i < len(mainlist[k]):
            if mainlist[k][i] == "X":
                if mainlist[k+1][i] == "M":
                    if mainlist[k+2][i] == "A":
                        if mainlist[k+3][i] == "S": 
                            return_value += 1 
            i += 1                            
        k += 1    
    return return_value

def vertikal_search_r_to_l(mainlist):
    return_value = 0

    k = 0
    while k < len(mainlist)-3:
        i = 0
        while i < len(mainlist[k]):
            if mainlist[k][i] == "S":
                if mainlist[k+1][i] == "A":
                    if mainlist[k+2][i] == "M":
                        if mainlist[k+3][i] == "X": 
                            return_value += 1 
            i += 1                            
        k += 1    
    return return_value

def diagonal_search__down_r_to_l(mainlist):
    return_value = 0

    k = 0
    while k < len(mainlist)-3:
        i = 0
        while i < len(mainlist[k])-3:
            if mainlist[k][i] == "X":
                if mainlist[k+1][i+1] == "M":
                    if mainlist[k+2][i+2] == "A":
                        if mainlist[k+3][i+3] == "S": 
                            return_value += 1 
            i += 1                            
        k += 1    
    return return_value
    
def diagonal_search__down_l_to_r(mainlist):
    return_value = 0

    k = 0
    while k < len(mainlist)-3:
        i = 0
        while i < len(mainlist[k])-3:
            if mainlist[k][i] == "S":
                if mainlist[k+1][i+1] == "A":
                    if mainlist[k+2][i+2] == "M":
                        if mainlist[k+3][i+3] == "X": 
                            return_value += 1 
            i += 1                            
        k += 1    
    return return_value

def diagonal_search__up_r_to_l(mainlist):
    return_value = 0

    k = 3
    while k < len(mainlist):
        i = 0
        while i < len(mainlist[k])-3:
            if mainlist[k][i] == "X":
                if mainlist[k-1][i+1] == "M":
                    if mainlist[k-2][i+2] == "A":
                        if mainlist[k-3][i+3] == "S": 
                            return_value += 1 
            i += 1                            
        k += 1    
    return return_value

def diagonal_search__up_l_to_r(mainlist):
    return_value = 0

    k = 3
    while k < len(mainlist):
        i = 0
        while i < len(mainlist[k])-3:
            if mainlist[k][i] == "S":
                if mainlist[k-1][i+1] == "A":
                    if mainlist[k-2][i+2] == "M":
                        if mainlist[k-3][i+3] == "X": 
                            return_value += 1 
            i += 1                            
        k += 1    
    return return_value
    