import os
import re
import requests
import string
from bs4 import BeautifulSoup


# Downloads the HTML content of a given URL and handles exceptions.
def download_html(url):
    try:
        r = requests.get(url)  # Send an HTTP GET request to the given URL
        r.raise_for_status()  # Raise an exception if the response contains an HTTP error status code
        return r.text  # Return the HTML content of the response
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")  # Print the error message
        return None


# Parses the HTML content and returns a set of absolute article links.
def articles_links_func(html, url):
    soup = BeautifulSoup(html, 'html.parser')  # Create a BeautifulSoup object to parse the HTML content
    links = set()  # Initialize an empty set to store unique article links

    # Iterate through all <a> elements with an href attribute
    for a in soup.find_all('a', href=True):
        link = a['href']

        # If the link is relative, prepend the base URL to create an absolute link
        if not link.startswith('http'):
            link = url + link

        links.add(link)  # Add the link to the set

    return links  # Return the set of absolute article links


# Cleans up a filename by removing invalid characters.
def sanitize_filename(filename):
    # Define a string of valid characters for a filename
    valid_characters = '-_.() %s%s' % (string.ascii_letters, string.digits)

    # Filter out any invalid characters in the filename and return the cleaned-up string
    return ''.join(c for c in filename if c in valid_characters)


# Downloads an article, extracts its content, and saves it as a text file.
def save_article(url, output_dir):
    html = download_html(url)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')

    # Find the title element, extract its text or use a default text if not found
    title = soup.find('h1', class_='gutter-top')
    title_text = title.get_text() if title else 'No title found'

    content_div = soup.find('div', id='divMainContent')
    if content_div:
        # Find all paragraph and list item elements within the content div
        paragraphs_and_list_items = content_div.find_all(['p', 'li'])
        content_text = ""

        # Iterate through the elements and clean up their content
        for element in paragraphs_and_list_items:
            # Remove all <img> elements within the paragraph or list item
            for img in element.find_all('img'):
                img.decompose()

            # Check if the element is not inside a container with class "btn btn-default"
            if not element.find_parent(class_="btn btn-default"):
                # Replace all <a> elements with their text followed by the URL in parentheses
                for a in element.find_all('a', href=True):
                    a.replace_with(f"{a.get_text()} ({a['href']})")

                # Append the cleaned-up element text to the content_text variable
                content_text += element.get_text() + "\n\n"
    else:
        content_text = "No content found"

        # Combine the title and content text
        extracted_text = f"{title_text}\n\n{content_text}"

        # Replace non-breaking spaces with regular spaces
        extracted_text = extracted_text.replace('\xa0', ' ')

        # Sanitize the filename using the URL's last part and append the '.txt' extension
        filename = sanitize_filename(url.split('/')[-1]) + '.txt'
        output_path = os.path.join(output_dir, filename)

        # Write the extracted text to a file in the specified output directory
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)

        print(f"Saved {url} to {output_path}")

# Iterates through a list of URLs and downloads articles for each category.
def download_articles(urls, output_dir):
    # Define a regex pattern to match the desired article URLs
    article_pattern = re.compile(r'https://itsupport\.ou\.edu/TDClient/\d+/Norman/KB')

    # Iterate through the provided list of URLs
    for url in urls:
        # Extract the base URL to be used for constructing absolute links from relative links
        base_url = '/'.join(url.split('/')[:3])

        # Download the HTML content of the current URL
        html = download_html(url)
        if not html:
            continue  # If the download failed, skip to the next URL

        # Extract article links from the downloaded HTML content
        article_links = articles_links_func(html, base_url)

        # Iterate through the extracted article links
        for link in article_links:
            # Check if the link matches the desired article URL pattern
            if article_pattern.match(link):
                # Save the article's content as a text file in the specified output directory
                save_article(link, output_dir)

# Define a list of URLs representing different categories on the IT support website
urls = ["https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=13", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=14",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=15", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=16",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=17", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=18",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=19", "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=20",
        "https://itsupport.ou.edu/TDClient/35/Norman/KB/?CategoryID=21"]

# Call the download_articles function with the list of URLs and the output directory 'articles_txt'
download_articles(urls, 'articles_txt')