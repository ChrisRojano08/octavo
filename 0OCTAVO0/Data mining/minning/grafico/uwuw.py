import matplotlib.pyplot as plt

tablas_mostradas = {}
tabla_mostrada = None

def mostrar_tabla(event):
    global tabla_mostrada

    if event.xdata is not None and event.ydata is not None:
        x = event.xdata
        y = event.ydata

        if tabla_mostrada is not None:
            tabla_mostrada.xy = (x, y)
            plt.draw()

        if x > 3 and x < 5 and y > 7 and y < 9 :
            if tabla_mostrada is None:
                tabla_mostrada = tablas_mostradas[(x, y)]
                tabla_mostrada.set_visible(True)
                plt.draw()
        else:
            if tabla_mostrada is not None:
                for tabla_mostrada in tablas_mostradas.values():
                    tabla_mostrada.set_visible(False)
                plt.draw()


fig, ax = plt.subplots()

cid_motion = fig.canvas.mpl_connect('motion_notify_event', mostrar_tabla)

puntos = [(4, 8), (3.6, 7.6), (4.5, 8.5)]
datos_puntos = {
    (4, 8): [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    (3.6, 7.6): [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    (4.5, 8.5): [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
}

for punto in puntos:
    x, y = punto
    datos = datos_puntos[punto]
    formato_tabla = '\n'.join(['\t'.join(map(str, fila)) for fila in datos])
    tabla_mostrada = plt.text(x, y, formato_tabla, ha='left', va='top', bbox=dict(facecolor='white', alpha=0.8), visible=False)
    tablas_mostradas[punto] = tabla_mostrada

plt.scatter(4,8)
plt.scatter(3.5,7.5)
plt.scatter(4.5,8.5)
plt.axis([0, 15, 0, 15])
plt.show()