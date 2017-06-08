class Disc():
    def __init__(self, num, tower):
        self._num = num
        self._tower = tower
        self._w = 20*self._num+20
        self._h = 20
    def draw(self, check, xpos, ypos):
        rectMode(CENTER)
        if check:
            fill(255,0,0)
        else:
            fill(255,255,255)
        rect(xpos, ypos, self._w, self._h)
        
class Tower():
    def __init__(self, num_discs, tower_num):
        self._disclst = []
        self._size = num_discs
        self._tower_num = tower_num
        self._xpos = (width/4)*self._tower_num+8
        self._ypos = 400
        for i in range(self._size):
            self._disclst.append(Disc(self._size-i, self._tower_num))
        #print(self._disclst)
    def draw(self, num, check):
        fill(105,105,105)
        rectMode(CORNER)
        rect((width/4)*self._tower_num,100,15,300)
        for i in range(len(self._disclst)):
            if self._disclst[i] == self._disclst[-1]:
                self._disclst[i].draw(check, self._xpos, self._ypos - (i*20)-10)
            else:
                self._disclst[i].draw(False, self._xpos, self._ypos - (i*20)-10)
        
    def get_top(self):
        return self._disclst[-1]
    def pop(self):
        x = self._disclst.pop()
        self._size -= 1
        return x
    def push(self, disc):
        self._disclst.append(disc)
        self._size += 1

class Board():
    def __init__(self):
        self._pegs = [Tower(10,1), Tower(0,2), Tower(0,3)]
        self._selected = [False, False, False]
    def draw(self):
        counter = 1
        for i in self._pegs:
            i.draw(counter, self._selected[counter-1])
            counter += 1
    
def mouseClicked():
    global Board
    part = mouseX // (width//3)
    for i in range(len(Board._selected)):
        if Board._selected[i]:
            Board._selected[i] = False
            print(Board._selected)
            if Board._pegs[part]._size == 0 or Board._pegs[part].get_top()._num > Board._pegs[i].get_top()._num:
                x = Board._pegs[i].pop()
                Board._pegs[part].push(x)
            part = -1
            
    if part <= 3 and part >= 0 and Board._pegs[part]._size > 0:
        Board._selected[part] = True
        #print(Board._selected)
        
def setup():
    global Board
    global temp
    temp = False
    Board = Board()
    size(1000,500)

def draw():
    clear()
    global Board
    global temp
    background(220,220,220)
    fill(0)
    rectMode(CORNER)
    rect(0,400,1000,100)
    Board.draw()
    