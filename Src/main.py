import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from recorrerCarpetas import procesar_archivos_xlsm
#from OrganizaciónDeCarpetas import rename_long_filenames



def enviar_correo(ruta_archivo, destinatario, asunto, cuerpo):
    remitente = 'santiagorm@iris.com.co'
    password = 'vldy rhrm ywaa wsml'

    # Crear el objeto del mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Adjuntar el cuerpo del mensaje
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar el archivo
    adjunto = MIMEBase('application', 'octet-stream')
    with open(ruta_archivo, 'rb') as archivo:
        adjunto.set_payload(archivo.read())
    encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', f'attachment; filename={os.path.basename(ruta_archivo)}')
    mensaje.attach(adjunto)

    # Enviar el correo
    with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.send_message(mensaje)




def main():

    ruta_principal = 'todo\CarpetasPlantillasDesgloce0.0.1'


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
    


    body= f"""Buenas tardes.

Se adjunta el archivo con el desglose de accionistas para su revisión.

Este es un mensaje automático, por favor no responder a este correo.
Quedamos atentos ante cualquier consulta.
Saludos
                """
    enviar_correo("Resultado\\resultado desgloce accionistas.xlsx", "santiagorm@iris.com.co", "Envío de archivo – Desglose de Accionistas", body)




# Ejecutar el método main solo si el script es ejecutado directamente
if __name__ == '__main__':
    main()




    
