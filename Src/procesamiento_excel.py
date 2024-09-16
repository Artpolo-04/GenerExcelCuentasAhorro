import pandas as pd

def EstructuracionExcel(file_path):
    # Leer la hoja completa del archivo Excel
    df = pd.read_excel(file_path, sheet_name='Plantilla', header=None)

    # Crear df_company
    encabezados_company = df.iloc[1, 1:4].tolist()  # B2, C2, D2
    registro_company = df.iloc[2, 1:4].tolist()  # B3, C3, D3
    df_company = pd.DataFrame([registro_company], columns=encabezados_company)

    df_company_renamed = df_company.rename(columns={
        'TIPO ID': 'tipo id empresa',
        'ID': 'id empresa',
        'NOMBRE': 'nombre empresa'
    })

    # Crear encabezados para df_stakeholders
    encabezados_stakeholders = df.iloc[31, 1:5].tolist()  # B32, C32, D32, E32
    encabezados_stakeholders.append('nivel')  # Agregar la columna 'nivel'
    encabezados_stakeholders.append('EmpresaAsociadaNivel')  # Agregar la columna 'EmpresaAsociadaNivel'

    # Inicializar lista para almacenar los registros
    registros_stakeholders = []

    # Inicializar posición de inicio y nivel
    inicio_tbl_stakeholders = 32
    nivel = 1

    # Leer los registros en bloques de 25 filas
    while True:
        # Leer un bloque de registros incluyendo la columna I (índice 8)
        bloque = df.iloc[inicio_tbl_stakeholders:inicio_tbl_stakeholders + 19, [1, 2, 3, 4, 8]].values

        # Verificar si el bloque está vacío (todos los elementos son nulos)
        if pd.isna(bloque).all():  # Si todos los elementos son nulos
            break  # Detener si el bloque está vacío
        else:
            bloque_no_vacio = []
            for row in bloque:
                if pd.isna(row).all():  # Si toda la fila es nula
                    print(f"Archivo Procesado: {file_path}")
                    break  # Detener si se encuentra una fila nula
                else:
                    # Separar los valores principales y el valor de 'EmpresaAsociadaNivel'
                    valores_principales = row[:-1].tolist()  # Los valores de B a E
                    empresa_asociada_nivel = row[-1]  # Valor de la columna I
                    
                    # Agregar el nivel y 'EmpresaAsociadaNivel' al registro
                    registro_con_nivel = valores_principales + [nivel, empresa_asociada_nivel]
                    bloque_no_vacio.append(registro_con_nivel)
            
            # Incrementar el nivel para el siguiente bloque
            nivel += 1

            if not bloque_no_vacio:
                break  # Detener si no hay registros válidos en el bloque

            registros_stakeholders.extend(bloque_no_vacio)  # Agregar registros no vacíos

        # Actualizar la posición de inicio para el siguiente bloque
        inicio_tbl_stakeholders += 26

    # Crear el DataFrame df_stakeholders
    df_stakeholders = pd.DataFrame(registros_stakeholders, columns=encabezados_stakeholders)
    df_company_renamed
    company_info = df_company_renamed.iloc[0]
    # Repetir los valores de company_info en todos los registros de df_stakeholders_con_nivel
    for col in company_info.index:
        df_stakeholders[col] = company_info[col]
    return df_stakeholders
