from prettytable import PrettyTable
import pandas as pd

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


control = 2
final = []
for i in range(1, 5):
    auxFinal = []

    itemSet = combinaciones(itemA, [], [], 0, 0, i)
    C_array = contar(data, itemSet)

    res = [x for x in C_array if x[1] >= control]
    
    for it in res:
        auxStr = ''
        for jt in it[0]:
            if ([x for x in items[0] if jt==x]):
                auxStr += dataColm[0]+'='+jt
            elif ([x for x in items[1] if jt==x]):
                auxStr += dataColm[1]+'='+jt
            elif ([x for x in items[2] if jt==x]):
                auxStr += dataColm[2]+'='+jt
            elif ([x for x in items[3] if jt==x]):
                auxStr += dataColm[3]+'='+jt
            elif ([x for x in items[4] if jt==x]):
                auxStr += dataColm[4]+'='+jt
            auxStr += ', '
        auxStr += '('+str(it[1])+')'
        auxFinal.append(auxStr)
    final.append(auxFinal)

lenghts = max([len(x) for x in final])

rows = []
for i in range(lenghts):
    axR = [' ' for x in range(len(dataColm))]

    axR[0] = str(i+1)

    for j in range(len(final)):
        if i < len(final[j]):
            axR[j+1] = final[j][i]
    rows.append(axR)

header = [' ']
header.extend([str(x+1)+'-item sets' for x in range(4)])
myTable = PrettyTable(header)
for row in rows:
    myTable.add_row(row)

with open('result.txt', 'w' ,encoding='utf8') as file:
    file.write(str(myTable))
    file.close()
