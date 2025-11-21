import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def cargar_datos_accidentes(ruta_archivo):
    """Carga los datos de accidentes de tránsito desde un archivo CSV."""
    try:
        df = pd.read_csv(ruta_archivo, low_memory=False)
        return df
    except Exception as e:
        print("Error cargando el archivo:", e)
        return None


def main():
    # Ruta del archivo de datos
    ruta = 'Datos/ACCIDENTES_DE_TRANSITO_DESDE_MARZO__2017_A_DICIEMBRE_DE_2022_20251120.csv'
    df = cargar_datos_accidentes(ruta)
    
    if df is not None:
        print("Datos cargados exitosamente:")
        print(df.head())
        print(f"\nForma del dataset: {df.shape}")
    
    # Importación perezosa de seaborn: solo cargar si se necesitan gráficos
    try:
        import seaborn as sns
        print("\nseaborn cargado correctamente. Puede añadir visualizaciones aquí.")
    except Exception as e:
        print(f"\nAviso: no se pudo importar seaborn: {e}")
        print("Para instalar en un entorno virtual:")
        print("  python -m pip install seaborn")


if __name__ == '__main__':
    main()

#empezamos con la limpieza de los datos 
def limpiar_datos(df):
    """Realiza limpieza básica de los datos."""

    #mostrar las 5 primeras filas
    print(df.head())

    # Eliminar filas duplicadas
    df = df.drop_duplicates()
    
    # Manejar valores nulos (ejemplo: eliminar filas con nulos)
    df = df.dropna()
    
    # Convertir columnas a tipos adecuados (ejemplo: fechas)
    if 'FECHA_ACCIDENTE' in df.columns:
        df['FECHA_ACCIDENTE'] = pd.to_datetime(df['FECHA_ACCIDENTE'], errors='coerce')
    
    return df
