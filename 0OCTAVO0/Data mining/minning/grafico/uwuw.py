import matplotlib.pyplot as plt

tablas_mostradas = {}
tabla_mostrada = None

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


fig, ax = plt.subplots()

cid_motion = fig.canvas.mpl_connect('motion_notify_event', mostrar_tabla)

puntos = [(4, 8), (5,9), (6,10)]
datos_puntos = {
    (4, 8): [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    (5, 9): [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    (6, 10): [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
}

for punto in puntos:
    x, y = punto
    datos = datos_puntos[punto]
    formato_tabla = '\n'.join([' '.join(map(str, fila)) for fila in datos])
    tabla_mostrada = plt.text(x, y, formato_tabla, ha='left', va='top', bbox=dict(facecolor='white', alpha=0.8), visible=False)
    tablas_mostradas[punto] = tabla_mostrada

plt.scatter(4, 8)
plt.scatter(5, 9)
plt.scatter(6, 10)
plt.axis([0, 15, 0, 15])
plt.show()