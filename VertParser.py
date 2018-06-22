def parseAdjMatrix(kek):
    OldList = kek.split('\n') # ['1 : 2 3 4', '2 : 1 5 6', '3 : 1 5 6', '4 : 1 5 6', '5 : 2 3 4']
    newList = [];
    for row in OldList:
        row = row[4:]
        ListMem = row.split(' ')
        for i, s in enumerate(ListMem):
            ListMem[i] = int(s) - 1;
        newList.append(ListMem)

    AdjMatrix = [[0 for i in range(0,len(newList))] for i in range(0,len(newList))]

    for index, row in enumerate(newList):
        for col in row: # row = [1,2,3], index = 0
            AdjMatrix[index][col] = 1;
            AdjMatrix[col][index] = 1;

    return AdjMatrix
