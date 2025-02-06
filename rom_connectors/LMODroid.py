from rom_connectors.utils import get_driver
from selenium.webdriver.common.by import By

# official, a non-official list is also avalaible
def getSupportedDevices():
    print("This one could take a while, don't worry")
    driver = get_driver('https://get.libremobileos.com/changes', wait_load_element_class='model')
    print("finally loaded")
    supported_devices = []
    # find all h3 with class "mb-4"
    elems = driver.find_elements(By.CLASS_NAME, 'model')
    for elem in elems:
        supported_devices.append(elem.get_attribute('innerHTML'))
    return supported_devices
