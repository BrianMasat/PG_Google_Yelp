import boto3
import os

aws_id = os.environ.get('aws_id')
aws_key = os.environ.get('aws_key')

# Nombre de la bucket de S3 y carpeta en S3
bucket_name = 'googleyelp-emr-bucket'
bucket_folder = 'Google_Yelp_Project/'

# Ruta absoluta en tu entorno local
local_folder = r'C:\Escritorio\PF\PG_Google_Yelp\Data-Lake'

# Configura la sesión de AWS
session = boto3.Session(
    aws_access_key_id=aws_id,
    aws_secret_access_key=aws_key,
)

def download_file(bucket_name, bucket_path, dest_path):
    print(f"Descargando archivo desde {bucket_path} a {dest_path}...")
    
    s3 = session.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.download_file(bucket_path, dest_path)

    print(f"Archivo descargado desde {bucket_path} a {dest_path}")

def get_files_objects(bucket_name, bucket_folder):
    s3_client = session.client("s3")
    all_objs = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=f"{bucket_folder}", Delimiter="/")

    files_objs = []

    for obj in all_objs.get('Contents', []):
        if obj['Key'] == bucket_folder:
            continue
        files_objs.append(obj)
    
    return files_objs

def download_all_files(bucket_name, bucket_folder, local_folder):
    files_objs = get_files_objects(bucket_name, bucket_folder)

    if not os.path.exists(local_folder):
        os.makedirs(local_folder)

    for obj in files_objs:
        bucket_file_path = obj['Key']
        file_name = os.path.basename(bucket_file_path)
        dest_path = os.path.join(local_folder, file_name)

        download_file(bucket_name, bucket_file_path, dest_path)

# Llamar a la función para descargar todos los archivos de 'Google Maps/'
download_all_files(bucket_name, 'Google_Yelp_Project/Google Maps/', local_folder)

# Llamar a la función para descargar todos los archivos de 'Yelp/'
download_all_files(bucket_name, 'Google_Yelp_Project/Yelp/', local_folder)

