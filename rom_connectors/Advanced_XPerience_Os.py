# get html of page https://axpos.org/dl.html


from bs4 import BeautifulSoup

from rom_connectors.utils import get_html


def getSupportedDevices():
    html = get_html('https://leech.binbash.rocks:8008/axp/')

    # parse html
    soup = BeautifulSoup(html, 'html.parser')
    # find all 'a' without class
    elem = soup.find_all('a', class_=None)
    supported_devices = []

    for e in elem:
        # get href of a
        href = e.get('href')
        if('http' not in href and '#' not in href and '?' not in href and '//' not in href and '.' not in href):
            supported_devices.append(href.split('/')[0])
    return supported_devices



