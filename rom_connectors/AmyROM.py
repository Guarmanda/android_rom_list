from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://sabrina.amyrom.tech/ota/')

    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find elem with id "items"
    item = soup.find(id='fallback')
    # in it, find all 'a' tags
    labels = item.find_all('a')
    for label in labels:
        # if href contains '/'
        if '/' in label.get('href'):
           supported_devices.append(label.text)
    return supported_devices
