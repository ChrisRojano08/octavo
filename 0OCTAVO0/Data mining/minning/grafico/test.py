import matplotlib.pyplot as plt
import numpy as np
import random

# Conectar puntos con una curva
def linea_curva(point1, point2):
    a = (point2[1] - point1[1])/(np.cosh(point2[0]) - np.cosh(point1[0]))
    b = point1[1] - a*np.cosh(point1[0])
    x = np.linspace(point1[0], point2[0], 100)
    y = a*np.cosh(x) + b

    return (x,y)


adV = [ [0,0,0,0,0],
        [0,0,0,0,0],
        [1,0,0,0,0], 
        [1,0,0,0,0] ]
rows = ['Contact','b','c','d']
cols = ['a1','b1','c1','d1','e1']

count = 0
for i in range(len(adV)):
    for j in range(len(adV[i])):
        if adV[i][j]==1:
            count+=1

points = {}
justPointsR = []
justPointsC = []
ys = 0
xs = 0
count= count*2
# Generar los puntos
for i in range(len(rows)):
    x = random.uniform(0, count)
    y = random.uniform(0, count)
    #points[rows[i]] = [x,y]
    #justPointsR.append([x,y])

    points[rows[i]] = [xs,ys]
    justPointsR.append([xs,ys])

    ys+=1
    xs+=1.5

# Generar los puntos
for i in range(len(cols)):
    x = random.uniform(0, count)
    y = random.uniform(0, count)
    #points[cols[i]] = [x,y]
    #justPointsC.append([x,y])

    points[cols[i]] = [xs,ys]
    justPointsC.append([xs,ys])

    ys+=1
    xs+=1.5

# Graficando puntos y añadiendoles etiqueta
plt.scatter([x[0] for x in justPointsR], [x[1] for x in justPointsR], s=500)
plt.scatter([x[0] for x in justPointsC], [x[1] for x in justPointsC], s=500)

for i in range(len(rows)):
    plt.text(justPointsR[i][0], justPointsR[i][1]+0.05, rows[i], va='bottom', ha='center')
for i in range(len(cols)):
    plt.text(justPointsC[i][0], justPointsC[i][1]+0.05, cols[i], va='bottom', ha='center')

# Graficando las conexiones entre los puntos segun la matriz de adyacencia
vertex = []
for i in range(len(adV)):
    for j in range(len(adV[i])):
        if adV[i][j]==1:
            #plt.plot( [points[rows[i]][0], points[cols[j]][0]], [points[rows[i]][1], points[cols[j]][1]] )

            x,y = linea_curva(points[rows[i]], points[cols[j]])
            plt.plot( x,y )


# Mostrando grafica cuadrada
plt.axis('square')
plt.show()
