import pandas as pd
import numpy as np

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def appendColms(contTbl):
    dfSharp=[]
    for i in range(len(contTbl)-1):
        a=[dataRow[i]]
        a.extend(contTbl[i])
        dfSharp.append(a)
    a=['Total']
    a.extend(contTbl[len(contTbl)-1])
    dfSharp.append(a)
    
    return dfSharp

dataframe = pd.read_excel('input.xlsx', sheet_name='data1')
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

    sums.append(sum([row[i] for row in data]))
sums.append(sum(sums))
contTbl.append(sums)

dfSharp = appendColms(contTbl)

colms = list(dataColm)
colms.append('Total')
df = pd.DataFrame(dfSharp, columns=colms)
with pd.ExcelWriter('output1.xlsx',mode='w') as writer:  
    df.to_excel(writer, sheet_name='Contingencia')

probTbl = np.empty([len(contTbl), len(contTbl[0])])
for i in range(len(contTbl)):
    for j in range(len(contTbl[i])):
        probTbl[i][j] = ''+str(contTbl[i][j]/contTbl[len(contTbl)-1][len(contTbl)-1])

dfSharp = appendColms(probTbl)
df = pd.DataFrame(dfSharp, columns=colms)
with pd.ExcelWriter('output1.xlsx',mode='a', engine='openpyxl') as writer:  
    df.to_excel(writer, sheet_name='Probabilidad', float_format="%.2f")
    
probMargin = np.empty([len(contTbl)-1, len(contTbl[0])])
for i in range(len(contTbl)-1):
    for j in range(len(contTbl[i])):
        probMargin[i][j] = ''+str(contTbl[i][j]/contTbl[i][len(contTbl)-1])
        
dfSharp=[]
for i in range(len(probMargin)):
    a=[dataRow[i]]
    a.extend(probMargin[i])
    dfSharp.append(a)
df = pd.DataFrame(dfSharp, columns=colms)
with pd.ExcelWriter('output1.xlsx',mode='a', engine='openpyxl') as writer:  
    df.to_excel(writer, sheet_name='Probabilidad Marginal 1', float_format="%.2f")
    
probMargin = np.empty([len(contTbl), len(contTbl[0])-1])
for i in range(len(contTbl)):
    for j in range(len(contTbl[i])-1):
       probMargin[i][j] = ''+str(contTbl[i][j]/contTbl[len(contTbl)-1][j])  
dfSharp = appendColms(probMargin)
df = pd.DataFrame(dfSharp, columns=colms[:-1])
with pd.ExcelWriter('output1.xlsx',mode='a', engine='openpyxl') as writer:  
    df.to_excel(writer, sheet_name='Probabilidad Marginal 2', float_format="%.2f")