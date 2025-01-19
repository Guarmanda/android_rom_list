from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://wiki.lineageos.org/devices/')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all a with href begining with '#device-'
    elems = soup.find_all('a', href=True)
    for elem in elems:
        if elem['href'].startswith('/devices/'):
            name = elem['href'].split('/')[2]
            # append elem.text before <small> tag
            supported_devices.append(name)
    # remove duplications
    supported_devices = list(set(supported_devices))
    # remove unknown
    supported_devices = list(filter(lambda a: a != 'unknown', supported_devices))
    supported_devices = list(filter(lambda a: a != '', supported_devices))
    return supported_devices
