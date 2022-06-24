#This uses graphics.py
from graphics import *
import random

def main():
    win = GraphWin("triangle", 999, 999)
    win.setBackground(color_rgb(255,255,255))
    
    #outer triangle vertices x,y starting in top left
    c = 499; d = 1 #d = 135 for equilateral
    e = 1; f = 998
    g = 998; h = 998
    
    #draw vertices
    Dot1 = Point(c,d)
    Dot1.draw(win)
    Dot2 = Point(e,f)
    Dot2.draw(win)
    Dot3 = Point(g,h)
    Dot3.draw(win)
    
    #random point coordinates
    a = random.randint(1,998)
    b = random.randint(1,998)
    
    n=0
    while n < 50000: #<-- number of dots drawn
        NewDot = Point(a,b)
        NewDot.draw(win)
        
        #spaghetti code but it works
        pick = random.randint(1,3)
        if pick == 1:
            NewDot2 = Point((c+a)/2,(d+b)/2)
            a = (c+a)/2
            b = (d+b)/2
            NewDot2.draw(win)
        if pick == 2:
            NewDot2 = Point((e+a)/2,(f+b)/2)
            a = (e+a)/2
            b = (f+b)/2
            NewDot2.draw(win)
        if pick == 3:
            NewDot2 = Point((g+a)/2,(h+b)/2)
            a = (g+a)/2
            b = (h+b)/2
            NewDot2.draw(win)
        n+=1
    win.getMouse()
    win.close()
    
main()
