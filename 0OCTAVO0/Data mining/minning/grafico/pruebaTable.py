import matplotlib.pyplot as plt

tabla_mostrada = None

def mostrar_tabla(event):
    global tabla_mostrada

    if event.xdata is not None and event.ydata is not None:
        x = event.xdata
        y = event.ydata

        if tabla_mostrada is not None:
            tabla_mostrada.xy = (x, y)
            plt.draw()

        if x > 3.8 and x < 4.2 and y > 7.8 and y < 8.2:
            if tabla_mostrada is None:
                datos = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

                formato_tabla = '\n'.join([' | '.join(map(str, fila)) for fila in datos])
                tabla_mostrada = plt.text(x, y, formato_tabla, ha='left', va='top', bbox=dict(facecolor='white', alpha=0.8))
                plt.draw()
        else:
            if tabla_mostrada is not None:
                tabla_mostrada.remove()
                tabla_mostrada = None
                plt.draw()

fig, ax = plt.subplots()

cid_motion = fig.canvas.mpl_connect('motion_notify_event', mostrar_tabla)
plt.scatter(4,8, s=100)
plt.axis([0, 15, 0, 15])

plt.show()