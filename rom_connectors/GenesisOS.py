import re
from utils import get_html

def getSupportedDevices():
    html = get_html('https://www.genesisos.dev/devices')

    # in html, codenames are like that :\"codename\":\"marble\"
    # we'll have to find them with regext or something like that
    supported_devices = []
    # Regex to match all codenames in the format \"codename\":\"value\"
    codename_matches = re.findall(r'\\?"codename\\?":\\?"(.*?)\\?"', html)
    return codename_matches
    