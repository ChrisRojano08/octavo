"""
    Creado por
        Christopher Rojano Jimenez
        Esau Abraham Meneses Baes
"""

import os
import pandas as pd
import numpy as np
import warnings
from openpyxl import load_workbook
warnings.simplefilter(action='ignore', category=FutureWarning)

def saveNew(dataF, nameSheet, startR):
    book = load_workbook('output.xlsx')
    writer = pd.ExcelWriter('output.xlsx', engine='openpyxl') 
    writer.book = book
    writer.sheets = {ws.title: ws for ws in book.worksheets}
    dataF.to_excel(writer, sheet_name=nameSheet, startrow=startR, index=False, float_format="%.2f")
    writer.save()
    writer.close()

def errorcheck(itemA,data,items):
    auxItems = [x[0] for sublist in itemA[:-1] for x in sublist]
    auxPoints = [x[0] for sublist in itemA[-1:] for x in sublist]
    finalist = []

    for x in auxItems:
        auxs = []
        for y in auxPoints:
            auxs.append([i for i in data if x in i if y in i])
        
        auxCount = [[auxPoints[i], len(auxs[i])] for i in range(len(auxs))]
        flAx = []
        flAx.append(str(x))
        flAx.extend(auxCount)

        finalist.append(flAx)

    listF = []
    for it in items:
        listAux = []
        for i in it:
            for fl in finalist:
                if i in str(fl[0]):
                    listAux.append(fl)
        listF.append(listAux)

    return [listF, finalist]

def generate(dataframe):
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
    colms = []

    [listError, listH] = errorcheck(itemA,data,items)
    for i in range(len(listError)):
        colmsDf = [' ']
        axDF = []
        for j in range(len(listError[i])):
            colmsDf.extend([x[0] for x in listError[i][j][1:] if x[0] not in colmsDf])

            valE = []
            valE.append(listError[i][j][0])
            valE.extend([x[1] for x in listError[i][j][1:]])

            axDF.extend([valE])
        
        d2 = pd.DataFrame(axDF)
        d2.columns = colmsDf
        result = pd.ExcelWriter('data/data_'+dataColm[i]+'.xlsx')
        d2.to_excel(result, index=False)
        result.save()
        colms.append(dataColm[i])
    return [colms, listError, itemA[len(itemA)-1], listH, dataColm[len(dataColm)-1]]

def appendColms(contTbl, dataRow):
    dfSharp=[]
    for i in range(len(contTbl)-1):
        a=[dataRow[i]]
        a.extend(contTbl[i])
        dfSharp.append(a)
    a=['Total']
    a.extend(contTbl[len(contTbl)-1])
    dfSharp.append(a)
    
    return dfSharp

def genProb(columnas):
    probs = []
    probsTbl = []
    for colm in columnas:
        startRow = 2

        dataframe = pd.read_excel('data/data_'+colm+'.xlsx')
        dataRow = dataframe.iloc[:, 0]
        dataColm = dataframe.columns.ravel()
        dataframe = dataframe.iloc[: , 1:]
        data = list(dataframe.values)
        contTbl = []
        sums = []
        for i in range(len(data)):
            axRw = 0
            for j in range(len(data[i])):
                axRw += data[i][j]
            
            axR = []
            axR.extend(data[i])
            axR.append(axRw)
            contTbl.append(axR)
        for i in range(len(np.array(data).T)):
            sums.append(sum([row[i] for row in data]))
        
        sums.append(sum(sums))
        contTbl.append(sums)
        dfSharp = appendColms(contTbl, dataRow)
        colms = list(dataColm)
        colms.append('Total')
        df = pd.DataFrame(dfSharp, columns=colms)

        if os.path.exists('output.xlsx'):
            with pd.ExcelWriter('output.xlsx',mode='a', engine='openpyxl') as writer:  
                df.to_excel(writer, sheet_name=colm, index=False, startrow=startRow)
        else:
            result = pd.ExcelWriter('output.xlsx',mode='w',engine='openpyxl')
            df.to_excel(result, index=False, startrow=startRow, sheet_name=colm)
            result.save()
        startRow += len(df)+3
        
        probTbl = np.empty([len(contTbl), len(contTbl[0])])
        for i in range(len(probTbl)):
            for j in range(len(probTbl[i])):
                probTbl[i][j] = ''+str(contTbl[i][j]/contTbl[len(contTbl)-1][len(contTbl[0])-1])
        dfSharp = appendColms(probTbl, dataRow)


        df = pd.DataFrame(dfSharp, columns=colms)
        saveNew(df, colm, startRow)
        startRow += len(df)+3
            
        probMargin = np.empty([len(contTbl)-1, len(contTbl[0])])
        for i in range(len(contTbl)-1):
            for j in range(len(contTbl[i])):
                probMargin[i][j] = ''+str(contTbl[i][j]/contTbl[i][len(contTbl[0])-1])
                
        dfSharp=[]
        for i in range(len(probMargin)):
            a=[dataRow[i]]
            a.extend(probMargin[i])
            dfSharp.append(a)
        
        df = pd.DataFrame(dfSharp, columns=colms)
        saveNew(df, colm, startRow)
        startRow += len(df)+3
            
        probMargin = np.empty([len(contTbl), len(contTbl[0])-1])
        probsTbl = np.empty([len(contTbl), len(contTbl[0])-1]).astype(str)
        probsTb = np.empty([len(contTbl), len(contTbl[0])-1]).astype(str)
        for i in range(len(contTbl)):
            for j in range(len(contTbl[i])-1):
                probMargin[i][j] = ''+str(contTbl[i][j]/contTbl[len(contTbl)-1][j])
                probsTbl[i][j] = ''+str(contTbl[i][j])+'/'+str(contTbl[len(contTbl)-1][j])
                probsTb[i][j] = ''+str(contTbl[i][j])

        dfSharp = appendColms(probMargin, dataRow)
        
        df = pd.DataFrame(dfSharp, columns=colms[:-1])
        saveNew(df, colm, startRow)

        dfSharpPr = appendColms(probsTbl, dataRow)
        dfPr = pd.DataFrame(dfSharpPr[:-1], columns=colms[:-1])

        dfSharpPrr = appendColms(probsTb, dataRow)
        dfPrr = pd.DataFrame(dfSharpPrr[:-1], columns=colms[:-1])
        
        probs.append([dfPrr, dfPr])
    return probs

mu = 1
dataFr = pd.read_excel('dataset-input_tenis.xlsx', sheet_name='dataText', converters={'windy':str})
[columnas, data, play, dataH, playN] = generate(dataFr)
probM = genProb(columnas)

dataframe = pd.read_excel('dataset-input_tenis.xlsx', sheet_name='prediccion', converters={'windy':str})
prediction = list(dataframe.values)
colums = dataframe.columns.ravel()
tot = sum(row[1] for row in play)

likeli = []
predic = []
head = []
for i in range(len(prediction)):
    likeliAx = []
    predicAx = []
    for j in range(len(play)):
        likeliAxS = 1
        
        if play[j][0] not in head:
            head.append(play[j][0])
        
        for attrEv in prediction[i]:
            idxAttr = [x[0] for x in dataH].index(attrEv)
            idxPlay = [x[0] for x in dataH[idxAttr]].index(play[j][0])
            likeliAxS *= ((dataH[idxAttr][idxPlay][1]+mu)/(play[j][1]+mu))
        likeliAx.append(likeliAxS * ((play[j][1]+mu) / (tot+mu)))
    likeliAx = [round((x*(1/sum(likeliAx)))*100, 2) for x in likeliAx]

    predicAx.extend(prediction[i])
    predicAx.extend(likeliAx)

    predic.append(predicAx)
    likeli.append(likeliAx)


colums = np.append(colums, [x for x in head])
d2 = pd.DataFrame(predic)
d2.columns = colums

with pd.ExcelWriter('output.xlsx',mode='a', engine='openpyxl') as writer:  
    d2.to_excel(writer, sheet_name='Predicciones', index=False)

colmsD = probM[0][0].columns.ravel()
evalSing = []
evalSing.append(' ')
evalProb = []
evalProb.append(' ')
for colEv in colmsD[1:]:
    evalSing.append( str(play[[x[0] for x in play].index(colEv.lower())][1]) )
    evalProb.append( str(play[[x[0] for x in play].index(colEv.lower())][1])+'/'+str(tot) )

evalSing = pd.DataFrame(evalSing).T
evalSing.columns = probM[0][0].columns.ravel()

evalProb = pd.DataFrame(evalProb).T
evalProb.columns = probM[0][0].columns.ravel()
probM.append([evalSing, evalProb])

lenghts = max([len(x[0]) for x in probM])
header = []
headerS = []
dataFin = []
firstColms = dataframe.columns.ravel()
firstColms = np.append(firstColms ,playN)
for i in range(len(probM)):
    dataAx = probM[i][0]
    subx = [' ' for x in range(len([x for x in probM[i][0]])) ]
    subx[int(len(subx)/2)] = firstColms[i].capitalize()
    subx.append(' ')

    for j in range(lenghts-len(probM[i][0])):
        emptyDict = {}
        for col in dataAx.columns.ravel():
            emptyDict[col] = ' '
        dataAx = dataAx.append(emptyDict, ignore_index=True)

    emptyDict = {}
    for col in dataAx.columns.ravel():
        emptyDict[col] = ' '
    dataAx = dataAx.append(emptyDict, ignore_index=True)

    dataAx = dataAx.append(probM[i][1])

    for j in range(lenghts-len(probM[i][0])):
        emptyDict = {}
        for col in dataAx.columns.ravel():
            emptyDict[col] = ' '
        dataAx = dataAx.append(emptyDict, ignore_index=True)
    
    dataFin.append((dataAx.values))
    headerS.append(list(dataAx.columns.ravel()))
    header.extend(subx)

yy = []
for i in range(len(dataFin)):
    y = []
    y.append(headerS[i])
    for elemt in dataFin[i]:
        y.append(elemt)
    yy.append(y)

dF = []
for j in range(len(yy[0])):
    dFAx = []
    for row in yy:
        dFAx.extend(row[j])
        dFAx.append(' ')
    dF.append(dFAx)

df = pd.DataFrame(dF)
df.columns = header
with pd.ExcelWriter('output.xlsx',mode='a', engine='openpyxl') as writer:  
    df.to_excel(writer, sheet_name='Probabilidades', float_format="%.2f", index=False)
