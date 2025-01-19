from rom_connectors.utils import get_driver
from selenium.webdriver.common.by import By

def getSupportedDevices():
    driver = get_driver("https://paranoidandroid.co/", wait_load_element_class="devilist")  
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []

    # find all a with class devilist
    devicesLinks = driver.find_elements(By.CLASS_NAME, "devilist")
    for elem in devicesLinks:
        # append only the part of href after /devices/
        supported_devices.append(elem.get_attribute('href').split('/')[-1])
    # remove duplicates
    supported_devices = list(dict.fromkeys(supported_devices))
    # close driver
    driver.quit()
    return supported_devices
