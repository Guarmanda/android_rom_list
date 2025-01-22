from bs4 import BeautifulSoup
from utils import get_html

def getSupportedDevices():
    html = get_html('https://halogenos.org/devices.html')

    soup = BeautifulSoup(html, 'html.parser')
    supported_devices = []
    # find all div with class 'card-header'
    elems = soup.find_all('div', class_='card-header')
    for elem in elems:
        # append elem.text before <small> tag
        supported_devices.append(elem.text)
    return supported_devices
