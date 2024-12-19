def findcursor(inputlist):
    k = 0
    while k < len(inputlist):
        i = 0
        while i < len(inputlist[k]):
            if inputlist[k][i] == "^":
                print(f"Cursor is at x= {i+1}, y= {k+1}")
                inputlist[k][i] = "."
                return inputlist,[i,k]
            i += 1
        k += 1

def moveup(current_file, cursor_position, counter):
        x = cursor_position[0]
        y = cursor_position[1]

        while y > 0:
            if current_file[y][x] == ".":
                    counter += 1
                    current_file[y][x] = "X"
            if current_file[y-1][x] != "#":
                #current_file[y-1][x] = "^"
                y -= 1
            else:
                print (f"dir: ^ avoid collision at x= {x+1}, y= {y+1}")
                return current_file , [x,y], counter
        print(f"exit at x{x} y{y} Counter: {counter}")
        return None

def movedown(current_file, cursor_position, counter):
        x = cursor_position[0]
        y = cursor_position[1]

        while y < len(current_file):
            if current_file[y][x] == ".":
                    counter += 1
                    current_file[y][x] = "X"
            if current_file[y+1][x] != "#":
                #current_file[y+1][x] = "^"
                y += 1
            else:
                print (f"dir v avoid collision at x= {x+1}, y= {y+1}")
                return current_file , [x,y], counter
        print(f"exit at x{x} y{y} Counter: {counter}")
        return None
            
def moveright(current_file, cursor_position,counter):
        x = cursor_position[0]
        y = cursor_position[1]

        while x < len(current_file[y]):
            if current_file[y][x] == ".":
                    counter += 1
                    current_file[y][x] = "X"
            if current_file[y][x+1] != "#":
                #current_file[y][x+1] = "^"
                x += 1
    
            else:
                print (f"dir > avoid collision at x= {x+1}, y= {y+1}")
                return current_file , [x,y], counter
        print(f"exit at x{x} y{y} Counter: {counter}")
        return None
        
def moveleft(current_file, cursor_position, counter):
        x = cursor_position[0]
        y = cursor_position[1]

        while x < len(current_file[y]):
            if current_file[y][x] == ".":
                    counter += 1
                    current_file[y][x] = "X"
            if current_file[y][x-1] != "#":
                #current_file[y][x-1] = "^"
                x -= 1
    
            else:
                print (f"dir < avoid collision at x= {x+1}, y= {y+1}")
                return current_file , [x,y], counter
        print(f"exit at x{x} y{y} Counter: {counter}")
        return None