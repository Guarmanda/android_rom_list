from utils import get_driver
from selenium.webdriver.common.by import By

# website not accessible with selenium or get_html... maybe it could work with a different user agent

#def getSupportedDevices():
#    driver = get_driver('https://get.hlcyn.co/builds', wait_load_element_class='bg-gray-100')
#
#    # with regexp, get everything between each "<a href="/vault/" and their next "/" in html
#    supported_devices = []
#    # find all a with href begining with '#device-'
#    elems = driver.find_elements(By.TAG_NAME, 'a')
#    for elem in elems:
#        print(elem)
#        #if elem['href'].startswith('/devices/'):
#        if elem.get_attribute('href').startswith('/devices/'):
#            name = elem.get_attribute('href').split('/')[2]
#            # append elem.text before <small> tag
#            supported_devices.append(name)
#    # remove ''
#    supported_devices = list(filter(lambda a: a != '', supported_devices))
#    return supported_devices
#
#print(getSupportedDevices())