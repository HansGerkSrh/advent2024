def x_checker(mainlist):
    return_value = 0

    k = 0
    while k < len(mainlist)-2:
        i = 0
        while i < len(mainlist[k])-2:
            if mainlist[k+1][i+1] == "A":
                if ((mainlist[k][i] == "M") and (mainlist[k+2][i+2] == "S")) or ((mainlist[k][i] == "S") and (mainlist[k+2][i+2] == "M")):
                    if ((mainlist[k][i+2] == "M") and (mainlist[k+2][i] == "S")) or ((mainlist[k][i+2] == "S") and (mainlist[k+2][i] == "M")):
                            return_value += 1 
            i += 1
        k += 1    
    return return_value