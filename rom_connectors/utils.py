import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET
import urllib3  
# or if this does not work with the previous import:
# from requests.packages import urllib3  

# Suppress only the single warning from urllib3.
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

def get_html(url):
    response = requests.get(url, verify=False)
    return response.text

# some websites needs to really open a browser to get the content, else they won't load the whole html
def get_driver(url, wait_load_element_id=None, wait_load_element_class=None, wait_load_element_tag=None):
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
    driver.get(url)
    
    if(wait_load_element_id):
        while True:
            try:
                driver.find_element(By.ID, wait_load_element_id)
                break
            except:
                time.sleep(1)
    if(wait_load_element_class):
        while True:
            try:
                driver.find_element(By.CLASS_NAME, wait_load_element_class)
                break
            except:
                time.sleep(1)
    if(wait_load_element_tag):
        while True:
            try:
                driver.find_element(By.TAG_NAME, wait_load_element_tag)
                break
            except:
                time.sleep(1)
    return driver

def get_source_forge_files_rss(original_url):
    # transform the url https://sourceforge.net/projects/ancientrom/files/ to 
    #https://sourceforge.net/projects/teamdarkness/rss
    url = original_url.split("files/")[0] + "rss"
    # parse xml
    response = requests.get(url)
    
    namespaces = {'media': 'http://video.search.yahoo.com/mrss/'}
    supported_devices = [] 
    et = ET.fromstring(response.text)
    # get all items
    items = et.findall('channel/item')
    for item in items:
        # we can get the size with media:content filesize attribute
        media = item.find('media:content', namespaces)
        size = media.get('filesize')
        # check if size is bigger than 200mb
        if int(size) > 200000000:
            media_url = media.get('url')
            # if media url beggins with original url,
            if media_url.startswith(original_url):
                folder_name = media_url.replace(original_url, "")
                folder_name = folder_name.split('/')[0]
                if folder_name not in supported_devices:
                    supported_devices.append(folder_name)
    return supported_devices
        
