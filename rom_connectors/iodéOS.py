from bs4 import BeautifulSoup
from utils import get_html

# official, a non-official list is also avalaible
def getSupportedDevices():
    html = get_html('https://iode.tech/fr/installation/')

    soup = BeautifulSoup(html, 'html.parser')
    supported_devices = []
    # find all td with class "column-2"
    elems = soup.find_all('td', class_='column-2')
    for elem in elems:
        # select text in parenthesys
        if('(' in elem.text and ')' in elem.text):
            text = elem.text.split('(')[1].split(')')[0]
            supported_devices.append(text)
        else:
            # the galaxy tab s5e does not have its codename specified but is on the page
            supported_devices.append("gts4lv")
    return supported_devices

