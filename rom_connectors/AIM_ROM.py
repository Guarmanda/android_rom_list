import requests
from bs4 import BeautifulSoup

# not working for the moment, device list is empty when using this technique

def get_html():
    url = 'https://aimrom.github.io/#download'
    response = requests.get(url)
    return response.text

def getSupportedDevices():
    html = get_html()
    print(html)
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []
    soup = BeautifulSoup(html, 'html.parser')
    elem = soup.find_all('devicename')
    for e in elem:
        value = str(e).replace('<devicename>', '').replace('</devicename>', '')
        supported_devices.append(value)
    return supported_devices

print(getSupportedDevices())