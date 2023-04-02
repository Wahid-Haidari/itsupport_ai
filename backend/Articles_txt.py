import os
from bs4 import BeautifulSoup

def clean_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the title and body content
    title = soup.title.string if soup.title else 'No title'
    body = soup.body.get_text(separator='\n', strip=True) if soup.body else 'No body content'

    # Combine the title and body content
    cleaned_content = f"{title}\n\n{body}"
    return cleaned_content

def save_as_txt(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as txt_file:
        txt_file.write(content)

folder_path = 'articles'
output_folder = 'articles_txt'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.html'):
            file_path = os.path.join(folder_path, file_name)
            cleaned_content = clean_html_file(file_path)
            output_file_name = f"{os.path.splitext(file_name)[0]}.txt"
            output_file_path = os.path.join(output_folder, output_file_name)
            save_as_txt(output_file_path, cleaned_content)
            print(f"Processed {file_path}, saved to {output_file_path}")