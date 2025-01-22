from bs4 import BeautifulSoup
from utils import get_html

def getSupportedDevices():
    html = get_html('https://grapheneos.org/releases')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find the a with href begining with '#device-'
    elems = soup.find_all('a', href=True)
    for elem in elems:
        if elem['href'].startswith('#device'):
            parent = elem.parent
            # remove elem from parent
            elem.extract()
            # in this href, find all other a
            for a in parent.find_all('a', href=True):
                # append their href minus the '#'
                supported_devices.append(a['href'][1:])
    return supported_devices

print(getSupportedDevices())

