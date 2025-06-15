import requests
from bs4 import BeautifulSoup

def fetch_blog(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    blog_container = soup.find("div", class_="EPigl")
    
    if not blog_container:
        return "Blog content not found."

    blog_texts = []

    for tag in blog_container.find_all(['p', 'h3', 'h4', 'span']):
        text = tag.get_text(strip=True)
        if text:
            blog_texts.append(text)

    return '\n\n'.join(blog_texts)