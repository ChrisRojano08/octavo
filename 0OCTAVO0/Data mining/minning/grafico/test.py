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


adV = [ [0,1,1,1],  [0,0,0,0],  [0,0,0,0] ]
nodes = ['a','b','c','d']

count = 0
for i in range(len(adV)):
    for j in range(len(adV[i])):
        if adV[i][j]==1:
            count+=1

points = {}
justPoints = []
ys = 0
xs = 0
# Generar los puntos
for i in range(len(nodes)):
    x = random.uniform(0, count)
    y = random.uniform(0, count)
    points[nodes[i]] = [x,y]
    justPoints.append([x,y])

    #points[nodes[i]] = [xs,ys]
    #justPoints.append([xs,ys])

    ys+=1
    xs+=0.5

# Graficando puntos y añadiendoles etiqueta
plt.scatter([x[0] for x in justPoints], [x[1] for x in justPoints], s=500)
for i in range(len(nodes)):
    plt.text(justPoints[i][0], justPoints[i][1]+0.05, nodes[i], va='bottom', ha='center')

# Graficando las conexiones entre los puntos segun la matriz de adyacencia
vertex = []
for i in range(len(adV)):
    for j in range(len(adV[i])):
        if adV[i][j]==1:
            plt.plot( [points[nodes[i]][0], points[nodes[j]][0]], [points[nodes[i]][1], points[nodes[j]][1]] )

            #x,y = linea_curva(points[nodes[i]], points[nodes[j]])
            #plt.plot( x,y )

# Mostrando grafica cuadrada
plt.axis('square')
plt.show()
