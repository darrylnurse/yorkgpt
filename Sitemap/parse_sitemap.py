import xml.etree.ElementTree as ET
from urllib.parse import urlparse
import os

# Load and parse the XML file
tree = ET.parse('sitemap.xml')
root = tree.getroot()

def create_title_from_path(path):
    # Extract the file name from the path
    file_name = os.path.basename(path)
    
    # Remove the file extension
    title = os.path.splitext(file_name)[0]
    
    # Replace hyphens with spaces and capitalize each word
    title = title.replace("-", " ").title()
    
    return title

# Iterate through each <url> entry in the sitemap
for url in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
    loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
    lastmod = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod").text
    
    parsed_url = urlparse(loc)
    domain = parsed_url.netloc
    path = parsed_url.path
    
    if '/image-repository/' in path:
        title = create_title_from_path(path)
        print(f"Title: {title}")
        print(f"URL: {loc}")
        print(f"Last Modified: {lastmod}")
        print("-" * 40)
    else:
        print(f"Domain: {domain}")
        print(f"Path: {path}")
        print(f"Last Modified: {lastmod}")
        print("-" * 40)
