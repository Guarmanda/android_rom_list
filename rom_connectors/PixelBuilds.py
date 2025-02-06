from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://pixelbuilds.org/download')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all span without any class
    table = soup.find_all('span')
    for elem in table:
        # if no class
        if(not elem.has_attr('class')) and not ' ' in elem.text:
            supported_devices.append(elem.text)
    return supported_devices