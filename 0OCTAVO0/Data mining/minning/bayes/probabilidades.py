import pandas as pd
import numpy as np

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class Probabilidades():
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

    def genProb(self, columnas):
        
        for colm in columnas:
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
            dfSharp = Probabilidades.appendColms(contTbl, dataRow)

            colms = list(dataColm)
            colms.append('Total')
            df = pd.DataFrame(dfSharp, columns=colms)
            with pd.ExcelWriter('output/output_'+colm+'.xlsx',mode='w') as writer:  
                df.to_excel(writer, sheet_name='Contingencia', index=False)

            probTbl = np.empty([len(contTbl), len(contTbl[0])])
            for i in range(len(probTbl)):
                for j in range(len(probTbl[i])):
                    probTbl[i][j] = ''+str(contTbl[i][j]/contTbl[len(contTbl)-1][len(contTbl[0])-1])

            dfSharp = Probabilidades.appendColms(probTbl, dataRow)
            df = pd.DataFrame(dfSharp, columns=colms)
            with pd.ExcelWriter('output/output_'+colm+'.xlsx',mode='a', engine='openpyxl') as writer:  
                df.to_excel(writer, sheet_name='Probabilidad', float_format="%.2f", index=False)
                
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
            with pd.ExcelWriter('output/output_'+colm+'.xlsx',mode='a', engine='openpyxl') as writer:  
                df.to_excel(writer, sheet_name='Probabilidad Marginal 1', float_format="%.2f", index=False)
                
            probMargin = np.empty([len(contTbl), len(contTbl[0])-1])
            for i in range(len(contTbl)):
                for j in range(len(contTbl[i])-1):
                    probMargin[i][j] = ''+str(contTbl[i][j]/contTbl[len(contTbl)-1][j])

            dfSharp = Probabilidades.appendColms(probMargin, dataRow)
            df = pd.DataFrame(dfSharp, columns=colms[:-1])
            with pd.ExcelWriter('output/output_'+colm+'.xlsx',mode='a', engine='openpyxl') as writer:  
                df.to_excel(writer, sheet_name='Probabilidad Marginal 2', float_format="%.2f", index=False)

