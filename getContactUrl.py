import re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


# URL to fetch HTML content from
def available_urls(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    html_content = str(soup.find_all())
    pattern = rf"{url}[\w\-\./?=&]+"

    urls = re.findall(pattern, html_content)
    unique_urls = set(urls)
    unique_urls.add(url)

    keywords = ["contact", "contact_us", "about"]

    for index_url in re.findall(r'href="([^"]+)"', html_content):
  
        complete_url = urljoin(url, index_url)
        if any(keyword in complete_url for keyword in keywords):
            unique_urls.add(complete_url)


    filtered_urls = [
        url for url in unique_urls
        if not re.search(r"\.[a-zA-Z0-9]+$", url) and any(keyword in url for keyword in keywords)
    ]
    filtered_urls.append(url)
    print(filtered_urls)
    return filtered_urls

