import shutil
import os
import urllib.parse
import re
import tempfile
import datetime

from jproperties import Properties
from file_utilities.file_lister import list_files_with_extension_and_prefix
from file_utilities.unzipper import download_and_unzip
from file_utilities.searcher import search_string_in_files
from file_utilities.email_sender import send_email
from file_utilities.oracle_table_manager import OracleTableManager

# Recuperar valores del config.properties


def load_config_properties():
    configs = Properties()

    with open('config.properties', 'rb') as config_file:
        configs.load(config_file, "utf-8")

    return configs

# Función para procesar un archivo ZIP


def process_zip_file(table_manager, zip_file_name, url, output_directory, configs):
    if not table_manager.check_file_exists(zip_file_name):
        print(f"Descargando y descomprimiendo {url}...")
        temp_dir = tempfile.mkdtemp(dir=output_directory)
        download_and_unzip(url, temp_dir)

        # Buscar contenido en los archivos y realizar acciones relacionadas
        print("Buscando contenido en archivos ... ")
        search_and_process_files(
            zip_file_name, temp_dir, configs, table_manager)

        # Insertar valores procesados en la tabla
        table_manager.insert_processed_values(zip_file_name)

        # Limpiar carpetas temporales
        print("Limpiando carpetas temporales ...")
        cleanup_temp_folders(output_directory)
        with open(results_file_path, "w") as file:
            file.truncate()

    else:
        print(f"El fichero {zip_file_name} ya ha sido procesado.")

# Función para procesar los resultados de búsqueda


def process_search_results(results, table_manager):

    alter_pattern = re.compile(r'ALTER TABLE\s+&?\w+\.\.(\w+)\s*.*')
    found_results = False  # Bandera para controlar si se encontraron resultados

    with open(results_file_path, "w") as results_file:
        for result in results:
            sql_statement = result[2]
            match = alter_pattern.search(sql_statement)
            if match:
                table_name = match.group(1)
                # Verificar si la tabla existe en la base de datos
                if table_manager.check_table_sga_exists(table_name):
                    results_file.write(
                        "Nombre de tabla afectada:" + table_name + "\n")
                    results_file.write(
                        "Fichero:" + result[0].split(os.path.sep)[-1] + "\n")
                    results_file.write(
                        "Línea:" + str(result[1]) + ":" + result[2] + "\n\n\n")
                    found_results = True  # Se encontraron resultados

        # Si no se encontraron resultados, escribir el mensaje correspondiente
        if not found_results:
            results_file.write("No se han encontrado resultados.\n")

# Función principal para buscar y procesar archivos


def search_and_process_files(zip_file_name, output_directory, configs, table_manager):
    reg_expression_files = configs.get("reg_expression_files").data
    search_results = search_string_in_files(
        output_directory, reg_expression_files)

    # Obtener datos de configuración
    subject = configs.get("subject").data
    message = configs.get("message").data + "\n\n " + zip_file_name
    to_email = configs.get("to_email").data

    if search_results:
        # Procesar los resultados de búsqueda
        process_search_results(search_results, table_manager)
    else:
        with open(results_file_path, "w") as file:
            file.write("No se han encontrado resultados.\n")

    send_email(subject, message, to_email, attachment_path=results_file_path)

# Función para limpiar carpetas temporales


def cleanup_temp_folders(output_directory):
    for folder_name in os.listdir(output_directory):
        folder_path = os.path.join(output_directory, folder_name)
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)


if __name__ == "__main__":

    configs = load_config_properties()
    url = configs.get("url").data
    decoded_url = urllib.parse.unquote(url)
    target_extension = configs.get("target_extension").data
    output_directory = configs.get("output_directory").data
    db_username = configs.get("db_username").data
    db_password = configs.get("db_password").data
    db_host = configs.get("db_host").data
    db_port = configs.get("db_port").data
    db_service = configs.get("db_service").data
    prefixes_to_filter_first = configs.get("prefixes_to_filter_first").data
    prefixes_to_filter_second = configs.get("prefixes_to_filter_second").data
    results_file_path = configs.get("results_file_path").data
    # Cambia a las cadenas que desees
    prefixes_to_filter = [prefixes_to_filter_first, prefixes_to_filter_second]

    file_urls = list_files_with_extension_and_prefix(
        url, target_extension, prefixes_to_filter)

    for url in file_urls:
        url = urllib.parse.unquote(url)
        zip_file_name = url.split('/')[-1]
        table_manager = OracleTableManager(
            db_username, db_password, db_host, db_port, db_service)

        process_zip_file(table_manager, zip_file_name, url,
                         output_directory, configs)

    # Obtén la fecha y hora actual
    fecha_actual = datetime.datetime.now()

    # Formatea la fecha como una cadena en el formato deseado
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")

    # Imprime el mensaje que incluye la fecha formateada
    print(f"Proceso finalizado con éxito. Fecha: {fecha_formateada}")
