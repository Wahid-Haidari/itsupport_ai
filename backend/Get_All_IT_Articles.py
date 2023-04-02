import string
import re

from bs4 import BeautifulSoup
import requests
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
    valid_characters = '-_.() %s%s' % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_characters)


def save_article(url, output_dir):
    html = download_html(url)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h1', class_='gutter-top')
    title_text = title.get_text() if title else 'No title found'

    content_div = soup.find('div', id='divMainContent')
    if content_div:
        paragraphs_and_list_items = content_div.find_all(['p', 'li'])
        content_text = ""
        for element in paragraphs_and_list_items:
            # Remove all <img> elements within the paragraph or list item
            for img in element.find_all('img'):
                img.decompose()

            if not element.find_parent(class_="btn btn-default"):
                # Replace all <a> elements with their text followed by the URL in parentheses
                for a in element.find_all('a', href=True):
                    a.replace_with(f"{a.get_text()} ({a['href']})")

                content_text += element.get_text() + "\n\n"
    else:
        content_text = 'No content found'

    extracted_text = f"{title_text}\n\n{content_text}"

    # Replace non-breaking spaces with regular spaces
    extracted_text = extracted_text.replace('\xa0', ' ')

    filename = sanitize_filename(url.split('/')[-1]) + '.txt'
    output_path = os.path.join(output_dir, filename)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(extracted_text)

    print(f"Saved {url} to {output_path}")

def download_articles(urls, output_dir):
    article_pattern = re.compile(r'https://itsupport\.ou\.edu/TDClient/\d+/Norman/KB')

    for url in urls:
        base_url = '/'.join(url.split('/')[:3])

        html = download_html(url)
        if not html:
            continue

        article_links = articles_links_func(html, base_url)

        for link in article_links:
            if article_pattern.match(link):
                save_article(link, output_dir)

urls = ["https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=13", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=14"
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=15", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=16",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=17", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=18",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=19", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=20",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=21"]

download_articles(urls, 'articles_txt')