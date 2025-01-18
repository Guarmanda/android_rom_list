from bs4 import BeautifulSoup
from flask import json
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://downloads.blissroms.org/')
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    # find elem with id active-visible-devices
    elem = soup.find_all(id='active-visible-devices') 
    #parse as json
    jsonObject = json.loads(elem[0].text)
    # the object is an array of object, in each object we have a 'codename' key
    for device in jsonObject:
        supported_devices.append(device['codename'])
    return supported_devices

