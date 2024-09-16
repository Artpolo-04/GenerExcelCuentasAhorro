import os
import pandas as pd
from recorrerCarpetas import procesar_archivos_xlsm
#from OrganizaciónDeCarpetas import rename_long_filenames

def main():
    '''
    # Llama a una funcion que cambia el nombre de los excel en caso de ser muy largos
    
    rename_long_filenames(ruta_principal)
    '''
    ruta_principal = 'CarpetasPlantillasDesgloce'


    df_stakeholders_general = procesar_archivos_xlsm(ruta_principal)
    
    # Obtener la ruta del directorio actual del script
    ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la ruta completa para la carpeta Resultado
    ruta_carpeta_resultado = os.path.join(ruta_proyecto, '..', 'Resultado')
    
    # Crear la carpeta Resultado si no existe
    if not os.path.exists(ruta_carpeta_resultado):
        os.makedirs(ruta_carpeta_resultado)
    
    # Ruta completa del archivo xlsm
    ruta_xlsm = os.path.join(ruta_carpeta_resultado, 'resultado.xlsx')
    
    # Guardar el DataFrame general en un archivo Excel (.xlsm)
    with pd.ExcelWriter(ruta_xlsm, engine='openpyxl') as writer:
        df_stakeholders_general.to_excel(writer, index=False, sheet_name='Datos')
    print(f'DataFrame guardado en {ruta_xlsm}')

# Ejecutar el método main solo si el script es ejecutado directamente
if __name__ == '__main__':
    main()




    
