from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://dl.omnirom.org/')
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find spans with class "name"
    table = soup.find_all('span', class_='name')
    for elem in table:
        # if text contain "/"
        if "/" in elem.text and "custom" not in elem.text:
            supported_devices.append(elem.text.split("/")[0])
    return supported_devices
