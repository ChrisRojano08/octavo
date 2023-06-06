import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

tablas_mostradas = {}
tabla_mostrada = None

# Funcion chida para agregar una curva
def linea_curva(point1, point2):
    a = (point2[1] - point1[1])/(np.cosh(point2[0]) - np.cosh(point1[0]))
    b = point1[1] - a*np.cosh(point1[0])
    x = np.linspace(point1[0], point2[0], 100)
    y = a*np.cosh(x) + b

    return (x,y)

# Evento que detecta la posicion del mouse y si esta
# en la lista de puntos se muestra la tabla
def mostrar_tabla(event):
    global tablas_mostradas

    if event.xdata is not None and event.ydata is not None:
        x = event.xdata
        y = event.ydata
        
        try:
            for tabla in tablas_mostradas.values():
                tabla.set_visible(False)
            
            tablas_mostradas[round(x),round(y)].set_visible(True)
            plt.draw()
        except:
            for tabla in tablas_mostradas.values():
                tabla.set_visible(False)
            plt.draw()

#Añadir el evento del mouse al grafico
fig, ax = plt.subplots()
cid_motion = fig.canvas.mpl_connect('motion_notify_event', mostrar_tabla)

#Leyendo matriz de adyacencia
dataframe = pd.read_excel('matriz_adyacencia1.xlsx')
dataColm = dataframe.columns.ravel()
data = list(dataframe.values)

# Dando formato a los datos para generar filas, columnas y matriz sola
adV = tuple([x[1:] for x in data])
rows = tuple([x[:1] for x in data])
rows = [str(x) for x in rows]
rows = [x.replace('\'','').replace(']','').replace('[','') for x in rows]
cols = tuple(dataColm[1:])

# Calculando numeros de puntos en la matriz
# para definir el tamaño de la ventana
count = 0
for i in range(len(adV)):
    for j in range(len(adV[i])):
        if adV[i][j]==1:
            count+=1

points = {}
justPointsR = []
justPointsC = []
ys = 2
xs = 2

# Generar los puntos
for row in rows:
    points[str(row)] = [xs,ys]
    justPointsR.append([xs,ys])

    ys+=1
    xs+=1

# Generar los puntos
for col in cols:
    points[str(col)] = [xs,ys]
    justPointsC.append([xs,ys])

    ys+=1
    xs+=1

# Graficando puntos
plt.scatter([x[0] for x in justPointsR], [x[1] for x in justPointsR], s=500, color='#B0D9F2')
plt.scatter([x[0] for x in justPointsC], [x[1] for x in justPointsC], s=500, color='#C1B0F2')

# Añadiendo etiquetas al grafico
for i in range(len(rows)):
    plt.text(justPointsR[i][0], justPointsR[i][1]+0.05, rows[i], va='bottom', ha='center')
for i in range(len(cols)):
    plt.text(justPointsC[i][0], justPointsC[i][1]+0.05, cols[i], va='bottom', ha='center')

# Graficando las conexiones entre los puntos segun la matriz de adyacencia
vertex = []
for i in range(len(adV)):
    for j in range(len(adV[i])):
        if adV[i][j]==1:
            x,y = linea_curva(points[str(rows[i])], points[str(cols[j])])
            plt.plot( x,y, 'k')

# Generar las tablas para los puntos de las filas
for punto in justPointsR:
    x, y = punto
    punto = (punto[0], punto[1])
    formato_tabla = '\n'.join([' | '.join(map(str, fila)) for fila in adV])
    tabla_mostrada = plt.text(x, y, formato_tabla, ha='left', va='top', bbox=dict(facecolor='white', alpha=0.8), visible=False)
    tablas_mostradas[punto] = tabla_mostrada

# Generar las tablas para los puntos de las columnas
for punto in justPointsC:
    x, y = punto
    punto = (punto[0], punto[1])
    formato_tabla = '\n'.join([' | '.join(map(str, fila)) for fila in adV])

    tabla_mostrada = plt.text(x, y, formato_tabla, ha='left', va='top', bbox=dict(facecolor='white', alpha=0.8), visible=False)
    tablas_mostradas[punto] = tabla_mostrada

# Mostrando grafica cuadrada
plt.axis('square')
plt.axis([0, xs+2, 0, xs+2])
plt.show()


