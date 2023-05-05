from bs4 import BeautifulSoup
import requests

def get_og_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    og_data = {}

    # Get og title
    og_title = soup.find('meta', property='og:title')
    if og_title and og_title.get('content'):
        og_data['title'] = og_title['content']

    # Get og description
    og_description = soup.find('meta', property='og:description')
    if og_description and og_description.get('content'):
        og_data['description'] = og_description['content']

    # Get og image
    og_image = soup.find('meta', property='og:image')
    if og_image and og_image.get('content'):
        og_data['image'] = og_image['content']

    return og_data
