from constants import *

def checkFinished(sourceDict,adjMatrix):
    for iElem in range(0,len(adjMatrix)-1):
        for jElem in range(0,len(adjMatrix)-1):
            NumberOfRed = 0
            NumberOfBlack = 0
            if adjMatrix[iElem][jElem] == 1:
                if sourceDict[iElem]['color'] == Color_Red:
                    NumberOfRed += 1
                if sourceDict[iElem]['color'] == Color_Black:
                    NumberOfBlue += 1
                if sourceDict[iElem]['color'] == Color_Blue:
                    return False
        if NumberOfRed != numRed: return False
        if NumberOfBlack != numBlack: return False
    return True
