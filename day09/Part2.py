"""
Task description: https://adventofcode.com/2024/day/9
"""

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


def block_update(inputlist):
    resultlist = []
    i = 0
    charindex = 0
    for chars in inputlist:
        resultlist.append([int(chars),[]])
        if i % 2 == 0:
            #verarbeitung Files
            k = 0
            while k < int(chars):
                resultlist[i][1].append(charindex)
                k += 1
            charindex += 1
            
        else:
            #verarbeitung Gaps
            k = 0
            while k < int(chars):
                resultlist[i][1].append(None)
                k += 1
            
        i += 1

    #print(resultlist)

    i = -1
    while abs(i) < len(resultlist):
        k = 1
        while k < len(resultlist):
            if resultlist[k][0] >= resultlist[i][0]:
                j = 0
                delcounter = 0
                while j < len(resultlist[k][1]) and (delcounter < resultlist[i][0]):
                    if resultlist[k][1][j] is None:
                        resultlist[k][1][j] = resultlist[i][1][delcounter]
                        resultlist[i][1][delcounter] = None
                        delcounter += 1
                    j += 1
                    
                resultlist[k][0] = resultlist[k][0] - resultlist[i][0]
                break
            k += 2
        i -= 2

    #print(resultlist)
    return resultlist


with open(r'day09/Input.txt', 'r') as text_file:
    text = text_file.read()
    inputlist = text



def calc_checksum(resultlist):
    numlist = []
    for i in resultlist:
        print(i)
        for number in i[1]:
            numlist.append(number)
    checksum = 0
    i = 0
    for num in numlist: 
        if num is not None: 
            checksum += i * num
        i += 1
    return checksum            


x = block_update("2333133121414131402")
print(calc_checksum(x))