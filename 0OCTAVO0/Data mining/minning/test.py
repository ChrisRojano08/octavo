def find_combinations(itemA, result, temp, i, j, n):
    if len(temp) == n:
        result.append(temp[:])
        temp = []
        return
    if i == len(itemA):
        return
    for k in range(j, len(itemA[i])):
        temp.append(itemA[i][k][0])
        find_combinations(itemA, result, temp, i+1, 0, n)
        temp.pop()
    find_combinations(itemA, result, temp, i+1, 0, n)

    return result

    

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


print((find_combinations(itemA, [], [], 0, 0, 2)))