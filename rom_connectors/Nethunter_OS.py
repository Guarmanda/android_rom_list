from bs4 import BeautifulSoup
from utils import get_html

def getSupportedDevices():
    html = get_html('https://nethunter.kali.org/images.html')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find elem with id pretty
    table = soup.find('table', id='pretty')
    for elem in table:
        # add second column to supported_devices
        supported_devices.append(elem.contents[1].text)
    return supported_devices

print(getSupportedDevices())

