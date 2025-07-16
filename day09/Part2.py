def block_update(inputlist):
    resultlist = []
    i = 0
    charindex = 0
    for chars in inputlist:
        resultlist.append([])
        if i % 2 == 0:
            #verarbeitung Files
            k = 0
            while k < int(chars):
                resultlist[i].append(charindex)
                k += 1
            charindex += 1
            
        else:
            #verarbeitung Gaps
            k = 0
            while k < int(chars):
                resultlist[i].append(None)
                k += 1
            
        i += 1
    return resultlist

#print(block_update("2333133121414131402"))

def determine_block_space (data_block:list):
    freepace_startpoint = 0
    for char in data_block:
        if char is not None:
            freepace_startpoint += 1
    block_space = len(data_block) - freepace_startpoint
    return block_space, freepace_startpoint

# x,y = determine_block_space([0,0,2,None,None,None,None])
# print(x,y)


def update_filesys(filelist):
    downcount = -1
    while abs(downcount) < len(filelist):
        if not determine_block_space(filelist[downcount])[0]:
            blocklenght = len(filelist[downcount])
            upcount = 0
            while upcount < len(filelist) + downcount:
                block_space, startpoint = determine_block_space(filelist[upcount])
                if block_space >= blocklenght:
                    i = 0
                    while i < len(filelist[downcount]):
                        filelist[upcount][startpoint] = filelist[downcount][i]
                        filelist[downcount][i] = None
                        i += 1
                        startpoint += 1
                    break
                upcount += 1
        downcount -= 1

    return filelist

def print_as_string(filelist):
    x = filelist
    retstring = ""
    for i in x:
        for char in i:
            if char is not None:
                retstring += str(char)
            else:
                retstring += "."  
    print(retstring)

def checksum(filelist):
    numlist = []
    for lists in filelist:
        for number in lists:
            numlist.append(number)

    i = 0
    returnsum = 0
    while i < len(numlist):
        if numlist[i] is not None:
            returnsum += i * numlist[i]
        i += 1

    return returnsum

with open(r'day09/Input.txt', 'r') as text_file:
    text = text_file.read()
    inputlist = text


input = inputlist
resultlist = block_update(input)
print(str(resultlist) + "\n")
filelist = update_filesys(resultlist)
print(str(filelist) + "\n")
sum = checksum(filelist)
print(sum)