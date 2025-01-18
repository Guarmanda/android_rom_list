from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://get.carbonrom.org/')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all 'a' with an href containing '/devices/'
    hrefs = soup.find_all('a', href=True)
    for href in hrefs:
        if('/device-' in href['href']):
            if(href['href'].split('-')[1].replace('.html', '') not in supported_devices):
                supported_devices.append(href['href'].split('-')[1].replace('.html', ''))
    return supported_devices


