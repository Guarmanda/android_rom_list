from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://wiki.pixelexperience.org/devices/')
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find spans with class "name"
    table = soup.find_all('span', class_='codename')
    for elem in table:
        supported_devices.append(elem.text)
    return supported_devices