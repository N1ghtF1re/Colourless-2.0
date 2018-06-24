import sys, random
from PyQt5.QtWidgets import QWidget,  QPushButton,QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from VertParser import parseAdjMatrix
from math import *
from constants import *
from checkGraph import checkFinished
from switchLevels import *
kek = '''1 : 2 3 4
2 : 1 5 6
3 : 1 5 6
4 : 1 5 6
5 : 2 3 4
6 : 2 3 4'''

kek2 = lotOfTrash[random.randint(1,3)]
adjMatrix = parseAdjMatrix(kek)

n = len(adjMatrix) # //VertexCount

vertexArr = [{'x':0, 'y':0, 'color':Color_Blue} for i in range(0,n)]

def calcCenter(size): # Вычисление координат центра окна
    dx = size.width()/2
    dy = size.height()/2
    return {'x':dx, 'y': dy}
def calcCoords(size, i): # Вычисление коориднат i-ой вершины по окружности
    center = calcCenter(size);
    dx = center['x']
    dy = center['y']
    x = r*cos( 2*pi*i/n - pi/2 ) - r0/2
    y = r*sin( 2*pi*i/n - pi/2 ) - r0/2
    return {'x': x, 'y': y}
def RelativeToAbsolute(size, coords): # Перевод из относительных (относительно центра) в абсолютные координаты
    center = calcCenter(size)
    return {'x':coords['x'] + center['x'], 'y':coords['y'] + center['y']}
def AbsoulteToRelative(size,coords): # Перевод из абсполютных в относительные координаты
    center = calcCenter(size)
    return {'x':coords['x'] - center['x'], 'y':coords['y'] - center['y']}

class ColourlessWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.btnApply = QPushButton("Я сделалъ", self)
        self.btnApply.clicked.connect(self.buttonClicked)
        self.CurrI = None; # Номер вершины, по которой кликнул пользователь (для перетаскивания)
        self.setGeometry(308, 300 , WIDTH, HEIGHT)
        self.setWindowTitle('SuperKekB')
        self.InitVertex()
        self.show()
#superKekB

    def paintEvent(self, e): # Событие перерисовки окна
        qp = QPainter()
        qp.begin(self)
        self.DrawLines(qp) # Отрисовка ребер
        self.drawVertex(qp) # Отрисовка вершин
        self.MoveButton(qp) # Перемещение кнопки в правый нижний угол
        qp.end()

    def MoveButton(self, qp): # Перемещение кнопки в правый нижний угол
        y = self.size().height() -  self.btnApply.size().height() - Padding
        x = self.size().width() - self.btnApply.size().width() - Padding
        self.btnApply.move(x,y)

    def buttonClicked(self): # При клике на кнопку - проверка раскраски
        print(checkFinished(vertexArr, adjMatrix))

    def InitVertex(self): # Первоначальное расположение вершин
        size = self.size() # Размер окна
        for v in range(0,n):
            coord = calcCoords(size, v); # Получение координат (относительно центра) расположения вершины на окружности
            vertexArr[v]['x'] = coord['x'] + r0 // 2 # vertexArr - список координат вершин
            vertexArr[v]['y'] = coord['y'] + r0 // 2

    def drawVertex(self, qp): # Отрисовка вершин при перерисовке окна
        col = QColor(0, 0, 0)
        col.setNamedColor('#000')
        pen = QPen(col, 1)
        qp.setPen(pen)
        size = self.size()
        for v in range(0,n): # n - количетсво вершин
            qp.setBrush(QColor(vertexArr[v]['color']))
            coords = vertexArr[v] # В vertexArr - координаты вершины
            coords = RelativeToAbsolute(size, coords) # переводим относительные в абсолютные координаты
            coords['x'] -= r0 // 2
            coords['y'] -= r0 // 2

            qp.drawEllipse(coords['x'], coords['y'], r0, r0) # Отрисовываем вершину

    def plotEdge(self, qp, i,j):
        size = self.size()
        coords1 =  RelativeToAbsolute(size,vertexArr[i]) # Переводим координаты двух вершин
        coords2 = RelativeToAbsolute(size,vertexArr[j]) # в абсолютные
        qp.drawLine(coords1['x'],coords1['y'], coords2['x'],coords2['y']) # соединяем две вершины линиями

    def DrawLines(self,qp):
        for i, row in enumerate(adjMatrix): # adjMatrix - матрица смежности
            for j, col in enumerate(row):
                if adjMatrix[i][j] == 1:
                    self.plotEdge(qp,i,j)

    def mousePressEvent(self, event):
        self.currI = None
        for index, vert in enumerate(vertexArr):
            x = event.pos().x()
            position = event.pos()
            y = event.pos().y()
            size = self.size()
            AbsoluteVert = RelativeToAbsolute(size,vert)
            r_xy = sqrt((AbsoluteVert['x'] - x)**2 + (AbsoluteVert['y'] - y)**2)
            if r_xy <= r0/2:
                self.currI = index
                if event.button() == Qt.RightButton:
                    vert['color'] = Color_Black
                else:
                    vert['color'] = Color_Red


        self.update()

    def mouseMoveEvent (self,event):
        x = event.pos().x()
        y = event.pos().y()
        size = self.size()
        if self.currI != None:
            newCoords={'x':x, 'y':y}
            newCoords = AbsoulteToRelative(size,newCoords)
            vertexArr[self.currI]['x'] = newCoords['x']
            vertexArr[self.currI]['y'] = newCoords['y']
        self.update()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ColourlessWindow()
    sys.exit(app.exec_())
