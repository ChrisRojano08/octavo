from prettytable import PrettyTable
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class GenerateProbabilities():
    def errorcheck(itemA,data,items):
        auxItems = [x[0] for sublist in itemA[:-1] for x in sublist]
        auxPoints = [x[0] for sublist in itemA[-1:] for x in sublist]
        finalist = []
        for x in auxItems:
            auxNo = [i for i in data if x in i if auxPoints[0] in i]
            auxYes = [i for i in data if x in i if auxPoints[1] in i]

            finalist.append([str(x), [str(auxPoints[1]), len(auxYes) ], [str(auxPoints[0]), len(auxNo) ] ])
        
        listF = []
        for it in items:
            listAux = []
            for i in it:
                for fl in finalist:
                    if i in str(fl):
                        listAux.append(fl)
            listF.append(listAux)
        
        return listF

    def generate(self):
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

        colms = []
        listError = GenerateProbabilities.errorcheck(itemA,data,items)
        for i in range(len(listError)):
            axDF = []
            for j in range(len(listError[i])):
                axDF.append([listError[i][j][0], listError[i][j][1][1], listError[i][j][2][1]])

            d2 = pd.DataFrame(axDF)
            d2.columns = [' ','Yes','No']
            result = pd.ExcelWriter('data/data_'+dataColm[i]+'.xlsx')
            d2.to_excel(result, index=False)
            result.save()
            colms.append(dataColm[i])

        return colms
