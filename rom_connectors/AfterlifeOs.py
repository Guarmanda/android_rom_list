from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


def getSupportedDevices():
    driver_path = "C:/Users/Admin/Desktop/chromedriver-win64/chromedriver.exe"  # Replace with your WebDriver's path

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("disable-gpu")
    options.headless = True
    options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    # Initialize the WebDriver (Chrome in this example)
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Open the target webpage
    url = "https://afterlifeos.com/device/"  # Replace with the actual URL
    driver.get(url)

    # check if the page is loaded
    while True:
        try:
            driver.find_element(By.ID, "brxe-oaesby")
            break
        except:
            time.sleep(1)
            
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
