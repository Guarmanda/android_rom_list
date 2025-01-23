import re
from rom_connectors.utils import get_html

def getSupportedDevices():
    html = get_html('https://www.genesisos.dev/devices')

    # Regex to match all codenames in the format \"codename\":\"value\"
    codename_matches = re.findall(r'\\?"codename\\?":\\?"(.*?)\\?"', html)
    return codename_matches
    