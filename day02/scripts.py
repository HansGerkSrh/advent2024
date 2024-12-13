
def decreasing_tester(linestring):
    i = 0
    while i < len(linestring)-1:
        if linestring[i] <= linestring[i+1] or abs((linestring[i+1])-linestring[i]) > 3:
            return False
        i += 1
    return True

def increasing_tester(linestring):
    i = 0
    while i < len(linestring)-1:
        if linestring[i] >= linestring[i+1] or abs(linestring[i+1]-(linestring[i])) > 3:
            return False
        i += 1
    return True