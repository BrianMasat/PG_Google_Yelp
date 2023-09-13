import boto3
import os

aws_id = os.environ.get('aws_id')
aws_key = os.environ.get('aws_key')

BUCKET_NAME = 'googleyelpdatawarehouse'
CARPETA_USUARIOS = r'C:\Escritorio\PF\PG_Google_Yelp\Data-Warehouse'

# Crear un cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_id,
    aws_secret_access_key=aws_key,
)

# Función recursiva para subir archivos en subdirectorios
def upload_files_recursive(folder_path, s3_bucket):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # Subir el archivo a S3 utilizando upload_file
            s3.upload_file(file_path, s3_bucket, f'Data Warehouse/{os.path.relpath(file_path, folder_path)}')
            print(f'Cargado: {file_path}')

# Llamar a la función recursiva para subir archivos
upload_files_recursive(CARPETA_USUARIOS, BUCKET_NAME)

print('Carga de todos los archivos completada')