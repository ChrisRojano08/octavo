import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def combinaciones(itemA, result, temp, i, j, n):
    if len(temp) == n:
        result.append(temp[:])
        temp = []
        return
    if i == len(itemA):
        return
    for k in range(j, len(itemA[i])):
        temp.append(itemA[i][k][0])
        combinaciones(itemA, result, temp, i+1, 0, n)
        temp.pop()
    combinaciones(itemA, result, temp, i+1, 0, n)

    return result

def contar(originV, vec):
    justIt = []
    Cc = []
    for items in vec:
        for col in originV:
            if (all(x in col for x in items)):
                if items not in justIt:
                    Cc.append([items, 1])
                    justIt.append(items)
                else:
                    Cc[justIt.index(items)][1] += 1
            else:
                if items not in justIt:
                    Cc.append([items, 0])
                    justIt.append(items)
    return Cc

dataframe = pd.read_excel('data.xlsx', converters={'windy':str}, sheet_name='dataText')
dataColm = dataframe.columns.ravel()
data = list(dataframe.values)

itemA = []
items = []
for i in range(len(data[0])):
    auxIt = []
    justI = []

    row = [row[i] for row in data]
    for cell in row:
        if cell in justI:
            auxIt[justI.index(cell)][1] += 1
        else:
            auxIt.append([cell, 1])
            justI.append(cell)
    items.append(justI)
    itemA.append(auxIt)


itemSet = combinaciones(itemA, [], [], 0, 0, 2)
print(itemSet)

