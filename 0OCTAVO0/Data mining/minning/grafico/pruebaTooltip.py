import matplotlib.pyplot as plt

imagen_mostrada = None

def mostrar_imagen(event):
    global imagen_mostrada
    
    if event.xdata is not None and event.ydata is not None:
        x = event.xdata
        y = event.ydata

        if x > 3.8 and x < 4.2 and y > 7.8 and y < 8.2:
            if imagen_mostrada is None:
                imagen = plt.imread('toolImg.png')
                imagen_mostrada = plt.imshow(imagen, extent=(x+0.2, x+2, y+0.2, y+2), zorder=10)
                plt.show()
        else:
            if imagen_mostrada is not None:
                imagen_mostrada.set_visible(False)
                plt.draw()
                imagen_mostrada = None

fig, ax = plt.subplots()

cid_motion = fig.canvas.mpl_connect('motion_notify_event', mostrar_imagen)
plt.scatter(4,8, s=100)
plt.axis([0, 15, 0, 15])

plt.show()