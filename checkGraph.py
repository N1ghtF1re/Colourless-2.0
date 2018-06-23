from constants import *

def checkFinished(sourceDict,adjMatrix):
    print(sourceDict)
    for iElem in range(0,len(adjMatrix)):
        NumberOfRed = 0
        NumberOfBlack = 0
        for jElem in range(0,len(adjMatrix)):
            if adjMatrix[iElem][jElem] == 1:
                if sourceDict[jElem]['color'] == Color_Red:
                    NumberOfRed += 1
                if sourceDict[jElem]['color'] == Color_Black:
                    NumberOfBlack += 1
                if sourceDict[jElem]['color'] == Color_Blue:
                    return False
        if NumberOfRed != numRed: return False
        if NumberOfBlack != numBlack: return False

    return True
