from rom_connectors.utils import get_html

# everything is on pling, links can be found in their telegram channel
def getSupportedDevices():
    html = get_html('https://raw.githubusercontent.com/ProjectEverest/everest-maintainers/14/everest.devices')
    supported_devices = html.split('\n')
    return supported_devices
