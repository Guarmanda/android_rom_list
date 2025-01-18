import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_html(url):
    response = requests.get(url)
    return response.text


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


def get_sourceforge_devices(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    # find all elems with class folder and with tag a
    elems = soup.find_all('a', class_='folder')
    #now in these elems, find the href
    supported_devices = []
    for e in elems:
        href = e.get('href')
        # from href replace "/stats/timeline" with ""
        href = 'https://sourceforge.net/'+href.replace("/stats/timeline", "")
        # visit the href
        html_href = get_html(href)
        print("checking folder " + href.replace("https://sourceforge.net/projects/", ""))
        # check if html contains "This folder has no files."
        if "This folder has no files." in html_href:
            continue
        else:
            if not check_folder_size_recursive(html_href):
                continue
            local_soup = BeautifulSoup(html_href, 'html.parser')
            # get elem of class "current-dir"
            elem = local_soup.find(class_='current-dir')
            supported_devices.append(elem.text)
    return supported_devices

def check_folder_size_recursive(html):
    local_soup = BeautifulSoup(html, 'html.parser')
    # get the folder size:
    # get all elems with property 'headers' that equals "files_size_h"
    size_elems = local_soup.find_all(attrs={'headers': 'files_size_h'})
    found_elem_bigger_than_200mb = False
    for size_elem in size_elems:
        # get the size of the folder
        size = size_elem.text
        # check if size is bigger than 200mb
        if "MB" in size:
            size = size.replace(" MB", "")
            size = float(size)
            if size > 200:
                found_elem_bigger_than_200mb = True
                return True
    if not found_elem_bigger_than_200mb:
        # check subfolders
        elems = local_soup.find_all('a', class_='folder')
        #now in these elems, find the href
        for e in elems:
            href = e.get('href')
            # from href replace "/stats/timeline" with ""
            href = 'https://sourceforge.net/'+href.replace("/stats/timeline", "")
            html_href = get_html(href)
            if "This folder has no files." in html_href:
                continue 
            else:
                return check_folder_size_recursive(html_href)
