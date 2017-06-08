import sys
import random
import math

def setup():
    size(1000, 700)
    background(255)
    pixelDensity(displayDensity())
    
def drawLineAngle(color, start, angle, length, width=1):
    angle += 180  # make up zero degrees
    end = (start[0] + math.sin(math.radians(angle)) * length,
           start[1] + math.cos(math.radians(angle)) * length)
    stroke(*color)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end

def drawLeaf(location):
        stroke(0, 50, 0)
        fill(100, 255, 100)
        strokeWeight(0.5)
        ellipse(location[0],location[1],15,15)
        
def drawTree(start,leaf):
        end = drawLineAngle((255,0,0),start,0,300)
        endL = drawLineAngle((0,255,255),end,25,300)
        endR = drawLineAngle((0,0,255),end,-25,300)
        if leaf:
            drawLeaf(endL)
            drawLeaf(endR)
            
def drawBasicTree(start, angle, leaf, width = 1, counter=0):
    counter += 1
    if counter > 10:
        return
    else:
        end = drawLineAngle((0,0,0),start,angle,20)
        drawBasicTree(end,angle + 20,leaf, width-5, counter)
        drawBasicTree(end,angle-20,leaf, width-5, counter)
        if leaf:
            drawLeaf(end)
            drawLeaf(end)

def drawBetterTree(start, angle, leaf, new_width = 20, new_length = 100,counter = 0):
    counter += 1
    global num
    if counter > 5:
        return
    else:
        end = drawLineAngle((0,0,0), start, angle, new_length, new_width)
        #new_coord = ( (end[0]+mouseX)/2, (end[1]+mouseY)/2 )
        drawBetterTree(end, angle+mouseX+20, leaf, new_width - 4, new_length-10,counter)
        drawBetterTree(end, angle+mouseY+20, leaf, new_width - 4, new_length-10,counter)
        if leaf:
            drawLeaf(end)
            drawLeaf(end)
            fill(0,0,0)
            text(str(num), end[0]-8, end[1]+5)
            num += 1

        '''
        if leaf and counter == 0:
            drawLeaf(end)
            drawLeaf(end)
        '''
#Color Start Angle Length Width
def keyPressed():
    global leaf
    if key=="l":
        leaf = not leaf

def setup():
    global leaf
    leaf=True

def draw():
    clear()
    background(255)
    global num
    num = 0
    #drawBasicTree((500,400), 0, leaf)
    drawBetterTree((500,650), 0, leaf)
    #drawTree2((500,400),0,leaf,20)