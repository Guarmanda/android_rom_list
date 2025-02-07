from rom_connectors.utils import get_driver
from selenium.webdriver.common.by import By

def getSupportedDevices():
    driver = get_driver("https://kaleidoscope.ink/download.html", wait_load_element_class="mdui-list-item")  
    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
    supported_devices = []

    # find all a with class devilist
    devicesLinks = driver.find_elements(By.TAG_NAME, "small")
    for elem in devicesLinks:
        name = elem.get_attribute('innerHTML')
        supported_devices.append(name)
    # close driver
    driver.quit()
    return supported_devices