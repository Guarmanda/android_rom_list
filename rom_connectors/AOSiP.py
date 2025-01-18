from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://aosip.weebly.com/downloads.html')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')

    # find elem with tag 'strong'
    item = soup.find_all('strong')

    for label in item:
        if(' ' not in label.text):
            supported_devices.append(label.text.lower())
    return supported_devices