from random import *
from tkinter import *
from VertParser import parseAdjMatrix
from math import *


def leftclick (event):
    print ('Lol')
    print(canvas.find_all())
def rightclick(event):
    print ('Вы нажали правую кнопку мыши')

kek = '''1 : 2 3 4
2 : 1 5 6
3 : 1 5 6
4 : 1 5 6
5 : 2 3 4
6 : 2 3 4'''

adjMatrix = parseAdjMatrix(kek)

HEIGHT = 400
WIDTH = 400

d = 5
dx = WIDTH/2
dy = HEIGHT/2
r = 40
r0 = 5
n = 10 # //VertexCount

size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()


def plotVertex(i):
    x = r*cos( 2*pi*i/n - pi/2 ) + dx
    y = r*sin( 2*pi*i/n - pi/2 ) + dy
    #circle( x,y,r0 )
    canvas.create_oval(x-r0,y-r0,x+r0,y+r0, fill='green')

for v in range(0,n):
    plotVertex(v);

def plotEdge(i,j):
    x1 = r*cos( 2*pi*i/n - pi/2 ) + dx
    y1 = r*sin( 2*pi*i/n - pi/2 ) + dy
    x2 = r*cos( 2*pi*j/n - pi/2 ) + dx
    y2 = r*sin( 2*pi*j/n - pi/2 ) + dy
    #line(x1,y1,x2,y2)

plotEdge(5,3)
plotEdge(0,8)
plotEdge(8,3)
plotEdge(7,3)




canvas.create_oval(30,30,60,60, fill='green')
k = canvas.create_oval(30,30,90,90, fill='green', width=2)
canvas.tag_bind(k, '<Button-1>', leftclick)
canvas.move(k,30,40)
root.mainloop()
