import os
from itertools import combinations

dataR = open('data.txt', encoding="utf8").read()
dataR = dataR.split('\n')

data = []
for line in dataR:
    aux = line.split(',')
    data.append(aux)

itemSet = []

itemA = []
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
    itemA.append(auxIt)


for i in range(len(itemA)):
    for j in range(len(itemA[i])):
        x = i+1
        y = j

        while x < len(itemA):
            y = 0
            while y < len(itemA[x]):
                print(str(itemA[i][j][0])+'+'+str(itemA[x][y][0]), end='/')
                y+=1
            x+=1
    print('')
    print('******')
 
for i in range(len(itemA)):
    for j in range(len(itemA[i])):
        x = i+1
        y = j

        for x in range(i+1, len(itemA)):
            for y in range(len(itemA[x])):
                print(str(itemA[i][j][0])+'+'+str(itemA[x][y][0]), end='/')
                
    print('')
    print('******')