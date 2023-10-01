import requests
from bs4 import BeautifulSoup
import hashlib

def get_content_and_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "", []
    
    if not response.headers['Content-Type'].startswith('text/html'):
        return "", []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.extract()

    #remove headers and footers
    for header in soup(["header", "footer"]):
        header.extract()

    text = " ".join(soup.stripped_strings)

    
    
    links = []
    for link in soup.find_all('a', href=True):
        link_url = link['href']
        # print(link_url)
        # Skip links that only contain fragments or just the root

        if link_url == '/' or link_url.startswith('/#'):
            continue

        # Convert relative URLs to absolute
        if not link_url.startswith(('http://', 'https://')):
            link_url = url + link_url  # this ensures that relative links are correctly appended
        links.append(link_url)
    
    return text, links

def save_text_to_file(text, url):
    # Use the hash of the URL to create a unique filename
    filename = 'data/' + hashlib.md5(url.encode()).hexdigest() + '.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def fetch_recursive(url, base_url, depth=2, visited=None):
    if depth == 0 or (visited and url in visited):
        return
    
    if visited is None:
        visited = set()

    print(url)
    visited.add(url)
    text, links = get_content_and_links(url)
    save_text_to_file(text, url)
    for link in links:
        fetch_recursive(link, base_url, depth=depth-1, visited=visited)

# Example
base_url = 'https://www.moveworks.com/sitemap'
fetch_recursive(base_url, base_url, depth=3)
