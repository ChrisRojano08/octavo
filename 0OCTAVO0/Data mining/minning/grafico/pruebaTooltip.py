import matplotlib.pyplot as plt

datos = [
    ["John Doe", 35, "Developer"],
    ["Jane Smith", 28, "Designer"],
    ["Bob Johnson", 42, "Manager"],
]

# Establecer los espaciados para las celdas de la tabla
x_start = 0.5
y_start = 0.5
x_spacing = 1.5
y_spacing = 0.5

# Crear la gráfica vacía
fig, ax = plt.subplots()

# Mostrar los datos de la tabla utilizando plt.text()
for i, fila in enumerate(datos):
    for j, valor in enumerate(fila):
        x = x_start + j * x_spacing
        y = y_start + i * y_spacing
        ax.text(x, y, str(valor), ha='left', va='center')

# Establecer los límites del gráfico
ax.set_xlim(0, x_start + len(datos[0]) * x_spacing)
ax.set_ylim(0, y_start + len(datos) * y_spacing)

# Ocultar los ejes
ax.axis('off')

# Mostrar la gráfica
plt.show()
