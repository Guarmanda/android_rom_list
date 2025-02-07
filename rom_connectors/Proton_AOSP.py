from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://protonaosp.org/download')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all "p" with class text-zinc-400
    table = soup.find_all('li')
    for elem in table:
        # if does not contain "Maintainer"
        if "(" in elem.text:
            supported_devices.append(elem.text.split("(")[1].split(")")[0])
    return supported_devices