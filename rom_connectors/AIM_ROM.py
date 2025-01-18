from utils import get_driver
from selenium.webdriver.common.by import By

def getSupportedDevices():
    
    driver = get_driver('https://aimrom.github.io/#download', wait_load_element_tag='devicename')
    
    elems = driver.find_elements(By.TAG_NAME, 'devicename')
    supported_devices = []
    for e in elems:
        supported_devices.append(e.text.lower())
    return supported_devices

print(getSupportedDevices())