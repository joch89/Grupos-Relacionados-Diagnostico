import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Especificar los tipos de datos de las columnas problemáticas
dtype_options = {'column26': str, 'column27': str, 'column28': str, 
'column29': str, 'column30': str, 'column31': str, 'column32': str, 
'column33': str, 'column47': str, 'column83': str, 'column84': str, 
'column85': str, 'column86': str, 'column87': str, 'column88': str, 
'column89': str, 'column90': str, 'column92': str}

# Cargar el conjunto de datos
df = pd.read_csv('C:\\Users\\josee\\OneDrive\\Documentos\\Proyectos Propios\\GRD\\Analisis de la Distribucion de los GRD\\Codigos agrupados top 20\\GRD_PUBLICO_2021.txt', sep='|', low_memory=False)

# Contar las ocurrencias de combinaciones de las columnas
counts = df.groupby(['DIAGNOSTICO1', 'DIAGNOSTICO2', 'PROCEDIMIENTO1', 'PROCEDIMIENTO2']).size().reset_index(name='COUNT')

# Ordenar en orden descendente por COUNT y seleccionar las 5 combinaciones más comunes
top_20_combinaciones = counts.sort_values(by='COUNT', ascending=False).head(20)

# Guarda la tabla como un archivo CSV
tabla_csv = top_20_combinaciones.to_csv('tabla.csv', index=False)

# Imprime un mensaje para confirmar que el archivo se ha guardado
print("La tabla se ha guardado en 'tabla.csv'")