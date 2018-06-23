import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from VertParser import parseAdjMatrix
from math import *

kek = '''1 : 2 3 4
2 : 1 3 5
3 : 1 2 6
4 : 1 7 8
5 : 2 7 9
6 : 3 10 11
7 : 4 5 12
8 : 4 9 10
9 : 5 8 12
10 : 6 8 11
11 : 6 10 12
12 : 7 9 11'''

adjMatrix = parseAdjMatrix(kek)
print(adjMatrix)
HEIGHT = 600
WIDTH = 600

d = 5

r = 200
r0 = 60 # радиус вершины
n = len(adjMatrix) # //VertexCount

vertexArr = [{'x':0, 'y':0, 'color':'#0000ff'} for i in range(0,n)]

def calcCenter(size):
    dx = size.width()/2
    dy = size.height()/2
    return {'x':dx, 'y': dy}

def calcCoords(size, i):
    center = calcCenter(size);
    dx = center['x']
    dy = center['y']
    x = r*cos( 2*pi*i/n - pi/2 ) + dx - r0/2
    y = r*sin( 2*pi*i/n - pi/2 ) + dy - r0/2
    return {'x': x, 'y': y}

def calcLineCoords(size, i, j):
    center = calcCenter(size);
    dx = center['x']
    dy = center['y']
    x1 = r*cos( 2*pi*i/n - pi/2 ) + dx
    y1 = r*sin( 2*pi*i/n - pi/2 ) + dy
    x2 = r*cos( 2*pi*j/n - pi/2 ) + dx
    y2 = r*sin( 2*pi*j/n - pi/2 ) + dy
    return {'x1' :x1, 'y1' : y1, 'x2':x2, 'y2': y2}

class ColourlessWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(308, 300 , WIDTH, HEIGHT)
        self.setWindowTitle('Points')
        self.show()


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.DrawLines(qp)
        self.drawVertex(qp)
        qp.end()

    def drawVertex(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#000')
        pen = QPen(col, 1)
        qp.setPen(pen)
        size = self.size()
        for v in range(0,n):
            coord = calcCoords(size, v);
            vertexArr[v]['x'] = coord['x'] + r0 // 2
            vertexArr[v]['y'] = coord['y'] + r0 // 2
            qp.setBrush(QColor(vertexArr[v]['color']))
            qp.drawEllipse(coord['x'], coord['y'], r0, r0)

    def plotEdge(self, qp, i,j):
        size = self.size()
        col = QColor(0, 0, 0)
        col.setNamedColor('#000')
        pen = QPen(col, 8)
        coords = calcLineCoords(size,i, j)
        qp.drawLine(coords['x1'],coords['y1'],coords['x2'],coords['y2'])

    def DrawLines(self,qp):
        for i, row in enumerate(adjMatrix):
            for j, col in enumerate(row): # row = [1,2,3], index = 0
                if adjMatrix[i][j] == 1:
                    self.plotEdge(qp,i,j)

    def mousePressEvent(self, event):
        for index, vert in enumerate(vertexArr):
            x = event.pos().x()
            y = event.pos().y()
            r_xy = sqrt((vert['x'] - x)**2 + (vert['y'] - y)**2)
            if r_xy <= r0/2:
                print(x,y,vert)
                if event.button() == Qt.RightButton:
                    vert['color'] = '#000000'
                else:
                    vert['color'] = '#ff0000'
                print(index)
        self.update()
        #print(event.pos().x())
        #print(vertexArr)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ColourlessWindow()
    sys.exit(app.exec_())
