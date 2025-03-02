from selenium.webdriver.common.by import By
from rom_connectors.utils import get_driver


def getSupportedDevices():
    html = get_driver('https://tequilaos.org/download', wait_load_element_class='text-accent2-50')
    # get elems of class _subtitle_kydio_79
    supported_devices = [] 
    # find input type checkbox and click on it
    html.find_element(By.TAG_NAME, 'input').click()
    elems = html.find_elements(By.CLASS_NAME, 'text-accent2-50')
    print(html)
    for elem in elems:
        if elem.text != 'Download' and ' ' not in elem.text and elem.text != '':
            supported_devices.append(elem.text)
    return supported_devices
