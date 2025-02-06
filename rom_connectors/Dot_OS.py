from rom_connectors.utils import get_driver
from selenium.webdriver.common.by import By

def getSupportedDevices():
    driver = get_driver("https://www.droidontime.com/devices", wait_load_element_id="menelinks")  
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []

    #elems = soup.find_all('a', href=True)
    # find all a with href begining with '/devices/'
    devicesLinks = driver.find_elements(By.XPATH, "//a[contains(@href, '/devices/')]")
    for elem in devicesLinks:
        # append only the part of href after /devices/
        supported_devices.append(elem.get_attribute('href').split('/')[4])
    return supported_devices
