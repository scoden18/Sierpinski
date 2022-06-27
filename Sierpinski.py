#This uses graphics.py
from graphics import *
import random
import math

def main():
    win = GraphWin("triangle", 1920, 1000)
    win.setBackground(color_rgb(255,255,255))
    
    #outer triangle vertices x,y starting in top left
    c = 960; d = 0
    e = 0; f = 1000
    g = 1920; h = 1000
    
    #draw vertices
    Dot1 = Point(c,d)
    Dot1.draw(win)
    Dot2 = Point(e,f)
    Dot2.draw(win)
    Dot3 = Point(g,h)
    Dot3.draw(win)
    
    #draw random point
    a = random.randint(1,1920)
    b = random.randint(1,1000)
    NewDot = Point(a,b)
    NewDot.draw(win)
    
    n=0
    while n < 50000: #<-- number of dots drawn
        pick = random.randint(1,3)
        if pick == 1:
            a = math.floor((c+a)/2)
            b = math.floor((d+b)/2)
            NewDot2 = Point(a,b)
            NewDot2.draw(win)
        if pick == 2:
            a = math.floor((e+a)/2)
            b = math.floor((f+b)/2)
            NewDot2 = Point(a,b)
            NewDot2.draw(win)
        if pick == 3:
            a = math.floor((g+a)/2)
            b = math.floor((h+b)/2)
            NewDot2 = Point(a,b)
            NewDot2.draw(win)
        n+=1
    win.getMouse()
    win.close()
    
main()
