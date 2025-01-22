from bs4 import BeautifulSoup
from utils import get_html

# official, a non-official list is also avalaible
def getSupportedDevices():
    html = get_html('https://kryptonproject.my.id/download/')

    soup = BeautifulSoup(html, 'html.parser')
    supported_devices = []
    # find all td with class "column-2"
    elems = soup.find_all('a', href=True)
    for elem in elems:
        if elem['href'].startswith('/download/') and ' ' not in elem.text:
            name = elem['href'].split('/')[2]
            # append elem.text before <small> tag
            supported_devices.append(name)
    return supported_devices

