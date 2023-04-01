import string

from bs4 import BeautifulSoup
import requests
import urllib.request
import os

def download_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

def articles_links_func(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for a in soup.find_all('a', href=True):
        link = a['href']
        if not link.startswith('http'):
            link = url + link
        links.add(link)

    return links

def sanitize_filename(filename):
    # Remove invalid characters from the filename
    valid_characters = '-_.() %s%s' % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_characters)

def save_article(url, output_dir):
    html = download_html(url)
    if not html:
        return

    # Sanitize the filename to avoid issues with special characters
    filename = sanitize_filename(url.split('/')[-1]) + '.html'
    output_path = os.path.join(output_dir, filename)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Saved {url} to {output_path}")

def download_articles(urls, output_dir):

    for url in urls:
        # Extract the base URL to handle relative links
        base_url = '/'.join(url.split('/')[:3])

        # Download the HTML content of the main URL
        html = download_html(url)
        if not html:
            continue

        # Get the article links from the downloaded HTML content
        article_links = articles_links_func(html, base_url)

        # Download and save each article to the output directory
        for link in article_links:
            save_article(link, output_dir)


urls = ["https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=13", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=14"
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=15", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=16",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=17", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=18",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=19", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=20",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=21"]

download_articles(urls, 'articles')