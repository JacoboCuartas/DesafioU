import pandas as pd

# Ruta completa al archivo
file_path = r"C:\Users\kb543\OneDrive\Documentos\Escritorio\Nueva carpeta\prueba\DesafioU\DesafioU\base_datos_salud.xlsx"

# Cargar datos
data = pd.read_excel(file_path, sheet_name="Sheet1")

# Promedio y desviación estándar de la columna "Capital"
promedio_capital = data["Capital"].mean()
desviacion_capital = data["Capital"].std()

print("Promedio de Capital:", promedio_capital)
print("Desviación estándar de Capital:", desviacion_capital)

# Cantidad de casos por clase de gasto
casos_por_clase = data["Expenditure_Class"].value_counts()
print("\nCantidad de casos por clase de gasto:")
print(casos_por_clase)

# Guardar el DataFrame en un nuevo archivo Excel
output_path = r"C:\Users\kb543\OneDrive\Documentos\Escritorio\Nueva carpeta\prueba\DesafioU\DesafioU\base_datos_salud_procesada.xlsx"
data.to_excel(output_path, index=False)

print(f"\nDataFrame guardado en: {output_path}")
