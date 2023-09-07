import os
import shutil

def cleanup(output_directory, temp_dir):
    # Eliminar los archivos descomprimidos
    for folder in os.listdir(output_directory):
        folder_path = os.path.join(output_directory, folder)
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            print(f"Se eliminó el directorio {folder_path}")

    print("Eliminación de archivos descomprimidos completada.")

    # Eliminar la carpeta temporal
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        print(f"Se eliminó el directorio temporal {temp_dir}")

    print("Eliminación de archivos temporales completada.")
