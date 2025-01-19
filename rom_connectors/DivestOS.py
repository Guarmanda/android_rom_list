from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://divestos.eeyo.re/pages/devices')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all a with href begining with '#device-'
    elems = soup.find_all('a', href=True)
    for elem in elems:
        if elem['href'].startswith('#device-'):
            # append elem.text before <small> tag
            supported_devices.append(elem.text.split(' ')[0])
    return supported_devices
