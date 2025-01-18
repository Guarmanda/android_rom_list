from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from utils import get_driver


def getSupportedDevices():
    driver = get_driver("https://afterlifeos.com/device/", wait_load_element_id="brxe-oaesby")  
            
    # check if elem of class fc-cta-do-not-consent is present, and click it if so
    try:
        driver.find_element(By.CLASS_NAME, "fc-cta-do-not-consent").click()
    except:
        pass

    # Scroll down to load dynamic content
    scroll_pause_time = 2  # Adjust pause time as needed
    for _ in range(10):  # Adjust the range for the desired amount of scrolling
        try:
            driver.find_element(By.ID, "brxe-oaesby").send_keys(Keys.END)  # Scroll to the bottom
            time.sleep(scroll_pause_time)
        except:
            try:
                driver.find_element(By.CLASS_NAME, "fc-cta-do-not-consent").click()
            except:
                pass
    phones = driver.find_element(By.ID, "brxe-oaesby")

    phones = phones.text
    # from phone.text, iterate lines. Keep first line, not second one, third one, not fourth one, and so on


    # Clean up
    driver.quit()
    
    suported_devices = []
    for i, line in enumerate(phones.splitlines()):
        if i % 2 == 0:
            suported_devices.append(line)
    return suported_devices
