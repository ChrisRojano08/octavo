from bokeh.plotting import figure, output_file, show

# Crear los datos para el gráfico
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Crear la figura
p = figure(title="Gráfico interactivo", x_axis_label='X', y_axis_label='Y')

# Agregar los datos al gráfico
p.line(x, y, legend_label='Linea', line_width=2)

# Generar el archivo de salida HTML
output_file("grafico_interactivo.html")

# Mostrar el gráfico en el navegador
show(p)