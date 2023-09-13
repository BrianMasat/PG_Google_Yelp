from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as rq
import boto3
import os

aws_id = os.environ.get('aws_id')
aws_key = os.environ.get('aws_key')

BUCKET_NAME = 'googleyelp-data'
CARPETA_USUARIOS = r'C:\Escritorio\PF\PG_Google_Yelp\Datos-Web-Scraping'

# Crear un cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_id,
    aws_secret_access_key=aws_key,
)

def run_etl():

    url_one = 'https://es.wikipedia.org/wiki/Anexo:Estados_de_los_Estados_Unidos_por_PIB'
    page_one = rq.get(url_one).text

    # Parseamos el html utilizando BeautifulSoup
    soup_one = bs(page_one, 'html.parser')
    table_one = soup_one.find('table')

    # Creamos un DataFrame vacio
    df_pbi = pd.DataFrame(columns=['estados', 'PBI (millones de $)', 'PBI nacional (% del total)', 'poblacion (millones)', 'PBI per capita ($)', 'ranking nacional'])

    # Obtenemos las filas de la tabla
    for row in table_one.find_all('tr')[1:]:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]

        if len(cols) >= 5:
            estados = cols[0]
            pbi_millones = cols[1]
            porcentaje_pbi = cols[2]
            poblacion = cols[3]
            pbi_per_capita = cols[4]
            ranking = cols[5]

            row_data = {'estados': estados, 'PBI (millones de $)': pbi_millones, 'PBI nacional (% del total)': porcentaje_pbi,
                        'poblacion (millones)': poblacion, 'PBI per capita ($)': pbi_per_capita, 'ranking nacional': ranking}
            df_pbi = pd.concat([df_pbi, pd.DataFrame([row_data])])

    df_pbi = df_pbi.iloc[1:]
    print(df_pbi)
    df_pbi.to_csv('C:\Escritorio\PF\PG_Google_Yelp\Datos-Web-Scraping\pbi.csv')

run_etl()


# Función recursiva para subir archivos en subdirectorios
def upload_files_recursive(folder_path, s3_bucket):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # Subir el archivo a S3 utilizando upload_file
            s3.upload_file(file_path, s3_bucket, f'Data Web-Scraping/{os.path.relpath(file_path, folder_path)}')
            print(f'Cargado: {file_path}')

# Llamar a la función recursiva para subir archivos
upload_files_recursive(CARPETA_USUARIOS, BUCKET_NAME)

print('Carga completada')