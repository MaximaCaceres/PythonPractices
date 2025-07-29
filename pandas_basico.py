import pandas as pd
import numpy as np 
import sys

print("--- Cargando Datos del CSV ---")

try:
    # pd.read_csv() es la función de Pandas para leer archivos CSV
    df_sensores = pd.read_csv('datos_sensores_ejemplo.csv') 

    print("Archivo CSV cargado exitosamente en un DataFrame.")
    print("Primeras 5 columnas del archivo:")
    print((df_sensores.head(5)))

    eleccion = int(input("\n¿Desea más información del archivo CSV? Pulse 1 para SÍ, o 0 para SALIR: "))
    if eleccion == 1:
            print("\n--- Mostrando más información del DataFrame... ---")
            print("\nInformación general (df.info()):")
            df_sensores.info() # Muestra un resumen conciso
            print("\nEstadísticas descriptivas (df.describe()):")
            print(df_sensores.describe()) # Muestra estadísticas básicas
    elif eleccion == 0:
            print("\nSaliendo del programa. ¡Hasta luego!")
            
            sys.exit() # sys.exit() termina la ejecución del scrip

except FileNotFoundError:

    print("Error: El archivo 'datos_sensores_ejemplo.csv' no se encontró.")
    print("Asegúrate de haberlo creado en la misma carpeta que este script.")

    exit() # Salir del programa si el archivo no se encuentra
