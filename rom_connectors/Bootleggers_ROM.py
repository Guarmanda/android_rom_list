from bs4 import BeautifulSoup
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://bootleggersrom-devices.github.io/')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')

    # find elem with class shishu-lighter-bg
    item = soup.find_all(class_='shishu-lighter-bg')

    for label in item:
        # if text contains ' |'  and text contains 'phone android', remove it and add to supported_devices
        if(' |' in label.text and 'phone_android' in label.text):
            label = label.text.split(' |')[0]
            # take only last word (after last space/tab)
            supported_devices.append(label.split()[-1].lower())
    return supported_devices


