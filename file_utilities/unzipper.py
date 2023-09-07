import os
import requests
import zipfile

def download_and_unzip(url, temp_dir):
    # Descargar el archivo ZIP
    response = requests.get(url)
    zip_filename = os.path.basename(url)
    zip_path = os.path.join(temp_dir, zip_filename)

    with open(zip_path, 'wb') as zip_file:
        zip_file.write(response.content)

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    # Eliminar el archivo ZIP después de descomprimirlo
    os.remove(zip_path)
