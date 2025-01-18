from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://crdroid.net/downloads')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all elem with class card-header
    elems = soup.find_all( class_='card-header')
    # for each simply add the text
    for elem in elems:
        supported_devices.append(elem.text)
    return supported_devices

