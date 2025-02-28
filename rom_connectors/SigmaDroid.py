from selenium.webdriver.common.by import By
from rom_connectors.utils import get_driver
# everything is on pling, links can be found in their telegram channel
def getSupportedDevices():
    html = get_driver('https://sigmadroid.xyz/Devices', wait_load_element_class='_subtitle_kydio_79')
    # get elems of class _subtitle_kydio_79
    supported_devices = [] 
    elems = html.find_elements(By.CLASS_NAME, '_subtitle_kydio_79')
    print(html)
    for elem in elems:
        supported_devices.append(elem.text.split('\n')[0])
    return supported_devices
