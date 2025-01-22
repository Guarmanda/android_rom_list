from utils import get_driver, get_html
from selenium.webdriver.common.by import By

def getSupportedDevices():
    driver = get_driver('https://havoc-os.com/download', wait_load_element_id='motorola')

    supported_devices = []

    # find all h2 with class 'text-gray-500'
    elems = driver.find_elements(By.TAG_NAME, 'h2')
    
    for elem in elems:
        if('text-gray-500' in elem.get_attribute('class') ):
            supported_devices.append(elem.text)
    return supported_devices
