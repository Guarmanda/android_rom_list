from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

# /!\ this sometimes not work: website sometimes down
def getSupportedDevices():
    html = get_html('https://cygnusos.com/downloadpage.html')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find all 'a' with href = #
    for a in soup.find_all('a', href=True):
        if a['href'] == '#':
            supported_devices.append(a.text)
    return supported_devices

