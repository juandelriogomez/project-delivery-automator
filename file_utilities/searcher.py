import os
import sys

def search_string_in_files(root_directory, search_string):
    results = []

    for root, _, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line_number, line in enumerate(f, start=1):
                    if search_string in line:
                        results.append((file_path, line_number, line.strip()))
    
    return results
