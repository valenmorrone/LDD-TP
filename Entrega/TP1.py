import pandas as pd
import openpyxl
import duckdb as dd
import numpy as np
#%%
carpeta = "/home/valen/Documentos/Facu/Labo_de_datos/TP1 LABO/"

centros_culturales = pd.read_csv(carpeta+'centros_culturales.csv')

centros_educativos = pd.read_excel(carpeta+'establecimientos_educativos.xlsx', skiprows=6)

censo = pd.read_excel(carpeta+'padron_poblacion.xlsX')
#%%

# for fila in censo:
#     inicio = 0
#     if "AREA" in fila[1]:
#         print(True)

repetidosDomicilio = centros_culturales['TipoLatitudLongitud'].value_counts()
repetidos = centros_culturales['Nombre'].isin(repetidosDomicilio.index)

#justificacion de clave centros culturales
for item in repetidos:
    if item == True:
        print("naonao")
print("done")


educativos_conteo = centros_educativos['Cueanexo'].value_counts() #justificacion de clave centros educativos
#%% PASAMOS MODELOS RELACIONALES


for fila in range(0, len(censo), 1):
    for item in range(0, len(censo.loc[fila]), 1):
        if 'AREA' in censo.loc[item]:
            cod_depto = censo.loc[item]
            nom_depto = censo.loc[item + 1] 