import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("datos.csv")

# Mostrar las primeras filas
print("Primeras filas del archivo:")
print(df.head())

# Mostrar estadísticas generales
print("\nResumen estadístico:")
print(df.describe())

# Mostrar los nombres de las columnas
print("\nColumnas del archivo:")
print(df.columns)

import matplotlib.pyplot as plt

# Agrupar por producto y sumar las cantidades
ventas_por_producto = df.groupby("producto")["cantidad"].sum()

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
ventas_por_producto.plot(kind="bar", color="skyblue", edgecolor="black")

# Títulos y etiquetas
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")
plt.xticks(rotation=45)
plt.tight_layout()

# 🔽 Guardar la imagen antes de mostrarla
plt.savefig("imagenes")

# Mostrar la gráfica
plt.show()

from PIL import Image

# Abrir la imagen de la gráfica
grafica = Image.open("imagenes")

# Abrir el logo
logo = Image.open("logo.png")

# Redimensionar el logo si es muy grande (opcional)
logo = logo.resize((100, 100))

# Posición donde irá el logo (esquina inferior derecha)
posicion = (grafica.width - logo.width - 10, grafica.height - logo.height - 10)

# Pegar el logo sobre la gráfica
grafica.paste(logo, posicion, mask=logo)  # usa 'mask' para respetar la transparencia

# Guardar la imagen final
grafica.save("grafica_con_logo.png")

print("✅ Imagen final guardada como 'grafica_con_logo.png'")
