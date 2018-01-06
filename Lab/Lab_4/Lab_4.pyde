import copy
import random
'''
def is_edge(x, y):
    if y==0:
        return "top"
    if y==height:
        return "bot"
    if x==0:
        return "left" 
    if x==width:
        return "right" 
    return False
'''
def neighbors(x,y):
    '''
    if is_edge(x,y) == "top":
        return [(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y)]
    elif is_edge(x,y) == "bot":
        return [(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y)]
    elif is_edge(x,y) == "left":
        return [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x+1,y)]
    elif is_edge(x,y) == "right":
        return [(x-1,y),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1)]
    else:
        return [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)]
    '''
    return [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)]

def update():
    #print("check")
    global grid_bool
    temp = copy.deepcopy(grid_bool)
    for row in range(len(grid_bool)):
        for col in range(len(grid_bool[row])):
            alive = 0
            for pos in neighbors(row,col):
                if grid_bool[pos[0]%60][pos[1]%80] == 1:
                    alive += 1
            if alive == 3:
                temp[row][col] = 1
            elif alive == 2 and grid_bool[row][col] == 1:
                temp[row][col] = 1
            else:
                temp[row][col] = 0
                
    grid_bool = temp
    
def display():
    #print("check2")
    global grid_bool
    x,y = 0,0
    for row in range(len(grid_bool)):
        for col in range(len(grid_bool[row])):
            if grid_bool[row][col] == 0:
                fill(255)
            else:
                fill(0)
            rect(x,y,w,h)
            x = x + w
        y = y + h
        x = 0
        
def randomize_new():
    global grid_bool
    temp = copy.deepcopy(grid_bool)
    for row in range(len(temp)):
        for col in range(len(temp[row])):
            x = random.randint(0,10)
            if x == 1:
                temp[row][col] = 1
            else:
                temp[row][col] = 0
    grid_bool = temp

def keyPressed():
    global paused
    if key == " ":
       paused = not paused
    if key == "n":
        for row in range(len(grid_bool)):
            for col in range(len(grid_bool[row])):
                grid_bool[row][col] = 0
    if key == "r":
        randomize_new()

def mouseClicked():
    if grid_bool[mouseY//10][mouseX//10] == 0:
        grid_bool[mouseY//10][mouseX//10] = 1
    elif grid_bool[mouseY//10][mouseX//10] == 1:
        grid_bool[mouseY//10][mouseX//10] = 0

def setup():
    global paused
    paused = False
    global grid_bool
    global w
    global h
    grid_bool = [[0]*(width/10) for n in range(height/10)]
    randomize_new()
    size(800,600)
    w = 10
    h = 10

def draw():
    display()
    if paused:
        return
    update()
    delay(5)