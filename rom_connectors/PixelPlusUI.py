from rom_connectors.utils import get_driver
from selenium.webdriver.common.by import By

# official, a non-official list is also avalaible
def getSupportedDevices():
    driver = get_driver('https://ppui.site/download', wait_load_element_class='code_name')
    supported_devices = []
    # find all h3 with class "mb-4"
    elems = driver.find_elements(By.CLASS_NAME, 'code_name')
    for elem in elems:
        supported_devices.append(elem.get_attribute('innerHTML').replace('(', '').replace(')', ''))
    return supported_devices
