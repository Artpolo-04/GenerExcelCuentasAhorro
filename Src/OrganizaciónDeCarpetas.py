'''import os
import pandas as pd

def rename_long_filenames(base_folder):
    # Recorre las carpetas en el directorio base
    for subfolder in os.listdir(base_folder):
        subfolder_path = os.path.join(base_folder, subfolder)

        # Verifica si es una carpeta
        if os.path.isdir(subfolder_path):
            # Recorre los archivos en la subcarpeta
            for file_name in os.listdir(subfolder_path):
                # Verifica si el archivo es un Excel (puedes ajustar esta comprobación si es necesario)
                if file_name.endswith('.xlsx') or file_name.endswith('.xls') or file_name.endswith('.xlsm'):
                    # Verifica si el nombre del archivo es mayor a 20 caracteres
                    if len(file_name) > 20:
                        # Construye las rutas de archivo
                        old_file_path = os.path.join(subfolder_path, file_name)
                        new_file_name = 'plantilla'
                        new_file_path = os.path.join(subfolder_path, new_file_name + os.path.splitext(file_name)[1])
                        
                        # Verifica si el archivo con el nuevo nombre ya existe
                        if os.path.exists(new_file_path):
                            try:
                                os.remove(new_file_path)
                                print(f'Archivo existente "{os.path.basename(new_file_path)}" eliminado de "{subfolder_path}"')
                            except Exception as e:
                                print(f'Error al eliminar el archivo existente "{os.path.basename(new_file_path)}": {e}')
                        
                        # Verifica si el archivo original existe antes de renombrar
                        if os.path.exists(old_file_path):
                            try:
                                os.rename(old_file_path, new_file_path)
                                print(f'Archivo "{file_name}" renombrado a "{os.path.basename(new_file_path)}" en "{subfolder_path}"')
                            except Exception as e:
                                print(f'Error al renombrar el archivo "{file_name}": {e}')
                        else:
                            print(f'Archivo original no encontrado: "{old_file_path}"')

# Llama a la función con la ruta de la carpeta principal
base_folder_path = 'D'
rename_long_filenames(base_folder_path)
'''