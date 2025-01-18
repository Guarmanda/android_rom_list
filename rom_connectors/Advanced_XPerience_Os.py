# get html of page https://axpos.org/dl.html


from bs4 import BeautifulSoup

from rom_connectors.utils import get_html


def getSupportedDevices():
    html = get_html('https://axpos.org/dl.html')

    # parse html
    soup = BeautifulSoup(html, 'html.parser')
    #get all elements with class single-service-area
    elem = soup.find_all(class_="single-service-area")
    # inside those elem, get the <h5> elements

    supported_devices = []

    for e in elem:
        # cast e as bs4.element.Tag
        e = BeautifulSoup(str(e), 'html.parser')
        # get the <h5> elements
        h5 = e.find('h5')
        # replace <h5> and ( ) and </h5> with empty string
        value = str(h5).replace('<h5>', '').replace('</h5>', '').replace('(', '').replace(')', '')
        if(value != 'None'):
            supported_devices.append(value)
    return supported_devices



