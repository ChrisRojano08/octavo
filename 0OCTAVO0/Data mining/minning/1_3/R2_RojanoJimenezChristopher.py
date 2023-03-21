from prettytable import PrettyTable
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

def errorcheck(itemA,data,dataR,items):
    auxItems = [x[0] for sublist in itemA[:-1] for x in sublist]
    auxPoints = [x[0] for sublist in itemA[-1:] for x in sublist]
    finalist = []
    for x in auxItems:
        auxNo = [i for i in data if x in i if auxPoints[0] in i]
        auxYes = [i for i in data if x in i if auxPoints[1] in i]
        if len(auxNo) > len(auxYes):
            finalist.append([str(x)+'->'+str(auxPoints[0]),str(len(auxYes))+'/'+str(len(auxNo)+len(auxYes))])
        else:
            finalist.append([str(x)+'->'+str(auxPoints[1]),str(len(auxNo))+'/'+str(len(auxNo)+len(auxYes))])
    listComplete = []
    listF = []
    for it in items:
        listAux = []
        for i in it:
            for fl in finalist:
                if i in str(fl):
                    listAux.append(fl)
        listF.append(listAux)
    for x in range(len(dataR)-1):
        auxTotal = 0
        auxTE = 0
        auxErrors = []
        auxRules = []
        for i in listF[x]:
            auxRules.append(i[0])
            auxErrors.append(i[1])
            auxTE +=int(i[1][:(i[1].find("/"))]) 
            auxTotal += int(i[1][(i[1].find("/")+1):])
        listComplete.append([dataR[x],auxRules,auxErrors,str(auxTE)+'/'+str(auxTotal)])
    return listComplete

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
items.pop()
listError = errorcheck(itemA,data,dataColm,items)
finalList = []
for l in listError:
    for r in range(len(l[1])):
        if r+1 == len(l[1]):
            finalList.append([l[0], l[1][r], l[2][r], l[3]])
        else:
            finalList.append([' ', l[1][r], l[2][r], ' '])
            
d2 = pd.DataFrame(finalList)
d2.columns = ['Attribute','Rules','Errors','Total errors']
result = pd.ExcelWriter('output2.xlsx')
d2.to_excel(result,'Errors')
result.save()