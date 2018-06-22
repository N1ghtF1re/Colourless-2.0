from random import *
from tkinter import *
from VertParser import parseAdjMatrix

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

size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()

canvas.create_oval(30,30,60,60, fill='green')
k = canvas.create_oval(30,30,90,90, fill='green', width=2)
canvas.tag_bind(k, '<Button-1>', leftclick)
canvas.move(k,30,40)
root.mainloop()
