# =====================================================================
# PROYECTO: ETL Pipeline & Analytics (Portfolio - Ventas Multi-tabla)
# 
# PSEUDOCÓDIGO / PLAN DE TRABAJO:
# 1. Configurar el entorno y las rutas blindadas para los archivos.
# 2. [EXTRACT]: Leer cada archivo CSV uno por uno.
# 3. [TRANSFORM]: Limpiar duplicados y nulos de forma explícita.
# 4. [LOAD]: Guardar cada tabla en SQLite con nombres claros (dim_ y fact_).
# 5. [VALIDATE]: Comprobar que los datos llegaron correctamente.
# =====================================================================
import os
import sqlite3
import pandas as pd

# PASO 1: Configurar rutas DECLARANDO LAS RUTAS:

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Directorio base
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data") # SUBCARPETA
db_path = os.path.join(DATA_DIR, "ventas_adventure.db") # ARCHIVO

#print(f"Ruta de la base de datos configurada en: {db_path}")

###########################################################################################

# PASO 2: [EXTRACT] - EXTRAER  DATOS ( no limpieza ojo)

camino_al_producto = os.path.join(DATA_DIR, "product.csv") # acceso a la ruta del producto

df_product = pd.read_csv(camino_al_producto, sep='\t', on_bad_lines='skip') # leemos la ruta del producto con panda saltando lineas malas y columnas \t


############################################################################################

# PASO 3: [TRANSFORM] - Limpieza de datos ( transformamos df_product paso a paso):

df_product = df_product.drop_duplicates() # eliminamos duplicados

# Como ya se separó bien, ahora sí podemos usar el nombre de la columna con total seguridad:

df_product["Product"] = df_product["Product"].fillna("Desconocido") # si se llama product dejala asi sino ponle desconocido y sigue 

#print(f"-> ¡Éxito total! Productos limpios. Filas totales: {len(df_product)}")

############################################################################################

# PASO 4 LOAD Guardar cada tabla en SQLite con nombres claros (dim_ y fact_)

# Abrimos la conexion sqlite3 a la bd  con la variable db_path:

conexion = sqlite3.connect(db_path)

# Guardamos el dataframe como una tabla SQL llamada dim_product:

df_product.to_sql('dim_product', conexion, if_exists = 'replace', index = False) # conecta la tabla llamada dim_product a SQL y si existe reemplazala

conexion.close() # cerramos conexion.

#print('Tabla dim_product creada exitosamente en la Base de datos ')

# ==========================================
# TABLA 2: DIM_REGION (Regiones) -> ¡Próximo paso!
# ==========================================

camino_a_la_region = os.path.join(DATA_DIR,'Region.csv')

df_regions = pd.read_csv(camino_a_la_region, sep='\t', on_bad_lines='skip')

#print("Columnas detectadas correctamente:", list(df_regions.columns))

df_regions = df_regions.drop_duplicates()

df_regions["Region"] = df_regions["Region"].fillna("Desconocido")

print(f"-> ¡Éxito total! Productos limpios. Filas totales: {len(df_regions)}")

conexion = sqlite3.connect(db_path)

df_regions.to_sql('dim_region', conexion, if_exists = 'replace', index = False)

conexion.close()

# ==========================================
# TABLA 3: FACT_SALES (Ventas / hechos) -> ¡Próximo paso!
# ==========================================

camino_a_las_ventas = os.path.join(DATA_DIR, 'Sales.csv') # RUTEAMOS EL ARCHIVO

df_sales = pd.read_csv(camino_a_las_ventas , sep= '\t', on_bad_lines = 'skip') #LEEMOS EL ARCHIVO SALTANDO ERRORES (EXTRACCION)

df_sales = df_sales.drop_duplicates()

df_sales['Sales'] = df_sales['Sales'].fillna(0) # CON CERO PORQUE ES UN MONTO NUMERICO

conexion = sqlite3.connect(db_path) #LOAD (CONEXION A SQL)

df_sales.to_sql('fact_sales', conexion, if_exists = 'replace', index = False)

conexion.close()

################COMPROBAR SI LAS TABLAS SE RELACIONAN BIEN ################################################

conexion = sqlite3.connect(db_path)
cursor = conexion.cursor()

query = ("""

SELECT 
    f.Quantity,
    p.Product,
    r.Region,
    f.Sales
FROM fact_sales f 
JOIN dim_product p ON f.ProductKey = p.ProductKey
JOIN dim_region r ON f.SalesTerritoryKey = r.SalesTerritoryKey
LIMIT 5;

""")

cursor.execute(query)
resultados = cursor.fetchall()

for fila in resultados:

    print(fila)








