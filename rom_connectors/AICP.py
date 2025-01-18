from bs4 import BeautifulSoup

from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://media.aicp-rom.com/vault/')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    elem = soup.find_all('a')
    for e in elem:
        if(e.get('href').startswith('/vault/')):
            value = str(e).replace('<a href="/vault/', '').replace('/', '')
            # remove everything after the first """ in value
            value = value.split('"')[0]
            supported_devices.append(value)
    return supported_devices

