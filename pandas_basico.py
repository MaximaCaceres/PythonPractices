import pandas as pd
import numpy as np 

print("--- Cargando Datos del CSV ---")

try:
    # pd.read_csv() es la función de Pandas para leer archivos CSV
    df_sensores = pd.read_csv('datos_sensores_ejemplo.csv') 

    print("Archivo CSV cargado exitosamente en un DataFrame.")
    print("Primeras 5 columnas del archivo:")
    print((df_sensores.head(5)))
    
except FileNotFoundError:

    print("Error: El archivo 'datos_sensores_ejemplo.csv' no se encontró.")
    print("Asegúrate de haberlo creado en la misma carpeta que este script.")

    exit() # Salir del programa si el archivo no se encuentra
