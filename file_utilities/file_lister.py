import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def list_files_with_extension_and_prefix(url, extension, prefixes=None):
    file_urls = []

    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            name = link.get_text()
            full_url = urljoin(url, link['href'])

            if name.endswith(extension) and (prefixes is None or any(name.startswith(prefix) for prefix in prefixes)):
                file_urls.append(full_url)
    
    return file_urls
