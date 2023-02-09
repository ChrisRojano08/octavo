import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

dataframe = pd.read_excel('data.xlsx', converters={'windy':str}, sheet_name='dataNum')
dataColm = dataframe.columns.ravel()
data = list(dataframe.values)

items = []
for i in range(len(data[0])):
    justI = []

    row = [row[i] for row in data]
    for cell in row:
        if cell not in justI:
            justI.append(cell)
    items.append(justI)

minimum = 3
a = len(items)-1
colClas = 2

data.sort(key=lambda row: (row[colClas]), reverse=False)
classes = [x for x in items[a]]
classesEx = [[x,0] for x in items[a]]

print(data)

rules = []
maxClas = []
auxElen = []
for i in range(len(data)):
    classesEx[classes.index(data[i][a])][1] += 1
    auxElen.append([data[i][colClas], data[i][a]])

    if any([x for x in classesEx if x[1] >= minimum]):
        if i<=len(data):
            if data[i+1][a]!=data[i][a]:
                classesEx = [[x,0] for x in items[a]]
                rules.append(auxElen)
                maxClas.append(data[i][a])
                auxElen = []
        else:
            classesEx = [[x,0] for x in items[a]]
            rules.append(auxElen)
            maxClas.append(data[i][a])
            auxElen = []
    
if len(auxElen)>0:
    if len(auxElen)==1:
        maxClas.append(auxElen[0][1])
    else:
        classesEx.sort(key=lambda row: (row[1]), reverse=False)
        maxClas.append(classesEx[0][0])
    
    rules.append(auxElen)

for rs in rules:
    print(rs)
print('')
print('********')

i=0
while i<len(maxClas)-1:
    if maxClas[i] == maxClas[i+1]:
        rules[i+1] = rules[i].extend(rules[i+1])
        rules.pop(i+1)
        maxClas.pop(i+1)
        i=0

        for rs in rules:
            print(rs)
        print('')
    else:
        i+=1

for rs in rules:
    print(rs)
print('')
print('********')

i=0
strRule = ''
for i in range(len(rules)-1):
    strRule += '  <=  '
    print('  <=  ', end='')
    strRule += str( (rules[i][len(rules[i])-1][0]+rules[i+1][0][0])/2 )+' --> '
    print(str( (rules[i][len(rules[i])-1][0]+rules[i+1][0][0])/2 ), end=' --> ')
    strRule += maxClas[i]
    print(maxClas[i], end='')

    strRule += '\n  >  '
    print('\n  >  ', end='')
    strRule += str( (rules[i][len(rules[i])-1][0]+rules[i+1][0][0])/2 )+' --> '
    print(str( (rules[i][len(rules[i])-1][0]+rules[i+1][0][0])/2 ), end=' --> ')
    strRule += maxClas[i+1]
    print(maxClas[i+1], end='')


df = pd.DataFrame({'Regla': [strRule]})
writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

