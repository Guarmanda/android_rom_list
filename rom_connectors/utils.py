import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET
import urllib3  
import os
# or if this does not work with the previous import:
# from requests.packages import urllib3  

# Suppress only the single warning from urllib3.
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

def get_html(url):
    response = requests.get(url, verify=False)
    return response.text

# some websites needs to really open a browser to get the content, else they won't load the whole html
def get_driver(url, wait_load_element_id=None, wait_load_element_class=None, wait_load_element_tag=None):
    current_path = os.path.dirname(os.path.realpath(__file__)) 
    # remove the last folder from the path
    current_path = os.path.dirname(current_path)
    driver_path = os.path.join(current_path, "brave_and_chrome_driver/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("disable-gpu")
    options.headless = True
    brave_binary = os.path.join(current_path, "brave_and_chrome_driver/brave.exe")
    options.binary_location = brave_binary
    
    # get the folder in same path of binary location
    folder = os.path.dirname(brave_binary)
    # get the folder in that folder
    for os_folder in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, os_folder)):
            # check if folder contains "chrome.dll"
            if not "chrome.dll" in os.listdir(os.path.join(folder, os_folder)):
                # download it from here https://www.dropbox.com/scl/fi/1zomv125qs322sjl7mgnz/chrome.dll?rlkey=5qdfx1viuc0r2nq7aabqw6k1z&st=8w5w8vha&dl=1
                # and put it in the folder
                print("chrome.dll not found in brave folder, downloading it from my personal dropbox...")
                download = requests.get("https://www.dropbox.com/scl/fi/1zomv125qs322sjl7mgnz/chrome.dll?rlkey=5qdfx1viuc0r2nq7aabqw6k1z&st=8w5w8vha&dl=1")
                with open(os.path.join(folder, os_folder, "chrome.dll"), "wb") as f:
                    f.write(download.content)
                print("chrome.dll downloaded")
    
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
        
