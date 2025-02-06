from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://nethunter.kali.org/images.html')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find elem with id pretty
    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        supported_devices.append(row.findAll('td')[2].contents[0].split("-")[0])
    return supported_devices


