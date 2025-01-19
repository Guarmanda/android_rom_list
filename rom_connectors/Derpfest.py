from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://derpfest.org/devices.html')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all h4 elemens
    for h4 in soup.find_all('h4'):
        # if h4 contains "(" and ")" then it is a device name
        if '(' in h4.text and ')' in h4.text:
            # append only the part between "(" and ")"
            supported_devices.append(h4.text[h4.text.find("(")+1:h4.text.find(")")])
    return supported_devices
