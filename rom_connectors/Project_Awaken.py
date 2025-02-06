from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://awakenos.vercel.app/downloads')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all "p" with class text-zinc-400
    table = soup.find_all('p', class_='text-zinc-400')
    for elem in table:
        # if does not contain "Maintainer"
        if "Maintainer" not in elem.text and " " not in elem.text: 
            supported_devices.append(elem.text)
    return supported_devices
