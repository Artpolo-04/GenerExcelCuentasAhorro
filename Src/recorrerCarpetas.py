import os
import pandas as pd
from procesamiento_excel import EstructuracionExcel

def procesar_archivos_xlsm(ruta_principal):
    # DataFrame general para acumular los resultados
    df_stakeholders_general = pd.DataFrame()

    # Recorrer cada carpeta en la ruta principal
    for carpeta in os.listdir(ruta_principal):
        ruta_carpeta = os.path.join(ruta_principal, carpeta)

        # Verificar si es una carpeta
        if os.path.isdir(ruta_carpeta):
            # Recorrer cada archivo en la carpeta
            for archivo in os.listdir(ruta_carpeta):  # Corrección aquí
                if archivo.endswith('.xlsm'):
                    ruta_archivo = os.path.join(ruta_carpeta, archivo)

                    try:
                        # Procesar el archivo con la función EstructuracionExcel
                        df = EstructuracionExcel(ruta_archivo)

                        # Resetear el índice para evitar problemas de duplicación
                        df = df.reset_index(drop=True)

                        # Acumular el DataFrame en el DataFrame general
                        df_stakeholders_general = pd.concat([df_stakeholders_general, df], ignore_index=True)
                    
                    except Exception as e:
                        # Registrar el error y continuar con el siguiente archivo
                        print(f"Error procesando el archivo {archivo}: {e}")
                        continue

    # Retornar el DataFrame general
    return df_stakeholders_general
