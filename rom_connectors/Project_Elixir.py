from utils import get_driver
from selenium.webdriver.common.by import By

def getSupportedDevices():
    driver = get_driver("https://projectelixiros.com/download", wait_load_element_class="card-subtitle")  
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []

    # find all a with class devilist
    devicesLinks = driver.find_elements(By.CLASS_NAME, "card-subtitle")
    for elem in devicesLinks:
        name = elem.get_attribute('innerHTML')
        if(' ' in name):
            name = name.split(' ')[0]
        # append only the part of href after /devices/
        supported_devices.append(name)
    # remove duplicates
    supported_devices = list(dict.fromkeys(supported_devices))
    # close driver
    driver.quit()
    return supported_devices

            