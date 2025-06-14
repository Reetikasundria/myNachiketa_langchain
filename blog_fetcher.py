import requests
from bs4 import BeautifulSoup

def fetch_blog(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    blog_texts = []

    for tag in soup.find_all(['p', 'h3', 'h4']):
        if tag.get_text(strip=True):
            blog_texts.append(tag.get_text(strip=True)) 

    for tag in soup.select('strong em, strong span, span strong em'):
        if tag.get_text(strip=True):
            blog_texts.append(tag.get_text(strip=True))

    full_blog = '\n\n'.join(blog_texts)
    return full_blog
