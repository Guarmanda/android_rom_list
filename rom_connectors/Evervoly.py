from bs4 import BeautifulSoup
from utils import get_html


def getSupportedDevices1(url):
    html = get_html(url)
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all a with href begining with '#device-' and with class list-group-item
    elems = soup.find_all('a', href=True, class_='list-group-item')
    for elem in elems:
        if elem['href'].startswith('/devices/'):
            name = elem['href'].split('/')[2]
            # append elem.text before <small> tag
            supported_devices.append(name)

    return supported_devices

def getSupportedDevices():
    return list(set(getSupportedDevices1('https://www.evervolv.com/devices/') + getSupportedDevices1('https://www.evervolv.com/devices/legacy')))
