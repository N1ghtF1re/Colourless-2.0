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

HEIGHT = 600
WIDTH = 600

d = 5
dx = WIDTH/2
dy = HEIGHT/2
r = 140
r0 = 20 # радиус вершины
n = len(adjMatrix) # //VertexCount


root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()


def plotVertex(i):
    x = r*cos( 2*pi*i/n - pi/2 ) + dx
    y = r*sin( 2*pi*i/n - pi/2 ) + dy
    #circle( x,y,r0 )
    k = canvas.create_oval(x-r0,y-r0,x+r0,y+r0, fill='green', width=0)


def plotEdge(i,j):
    x1 = r*cos( 2*pi*i/n - pi/2 ) + dx
    y1 = r*sin( 2*pi*i/n - pi/2 ) + dy
    x2 = r*cos( 2*pi*j/n - pi/2 ) + dx
    y2 = r*sin( 2*pi*j/n - pi/2 ) + dy
    canvas.create_line(x1,y1,x2,y2, width=3)


for index, row in enumerate(adjMatrix):
    for col in row: # row = [1,2,3], index = 0
        if adjMatrix[index][col] == 1:
            plotEdge(index,col)


for v in range(0,n):
    plotVertex(v);



#canvas.tag_bind(k, '<Button-1>', leftclick)
#canvas.move(k,30,40)
root.mainloop()
