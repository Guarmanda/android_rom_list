from rom_connectors.utils import get_driver
from selenium.webdriver.common.by import By

# official, a non-official list is also avalaible
def getSupportedDevices():
    driver = get_driver('https://komodo-os.my.id/download', wait_load_element_id='flush-collapse-8')
    supported_devices = []
    # find all h3 with class "mb-4"
    elems = driver.find_elements(By.TAG_NAME, 'h3')
    for elem in elems:
        if('mb-4' in elem.get_attribute('class') ):
            supported_devices.append(elem.get_attribute('innerHTML'))
    return supported_devices
