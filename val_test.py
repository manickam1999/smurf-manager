from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
DATA = ["a","a"]

def getData():
    global DATA
    with open("accounts.txt") as f:
        DATA = f.readlines()
    size = len(DATA) 
    for i in range(size):
        DATA[i] = DATA[i].strip('\n')

def writeData(new):
    open("accounts.txt","w").close()
    with open("accounts.txt","w") as f:
        for i in range(len(DATA)):
            f.write(new[i] + "\n")

getData()
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://tracker.gg/valorant")
new = ['A'] * len(DATA)
for i in range(len(DATA)):
    details = DATA[i].split(":")
    ign = details[0] + "#" + details[1]
    try:
        search_elem = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='search']"))
        )
        search_elem.send_keys(ign)
        search_elem.send_keys(Keys.RETURN)
    finally:
        '''donothing'''

    try:
        rank_elem = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CLASS_NAME,"rating-entry__info"))
        )
        rank = rank_elem.find_element_by_class_name("value").text
    except:
        rank = "Unrated"
    finally:
        new[i] = details[0] + ':' + details[1] + ':' + rank + ':' + details[3] + ':' + details[4]
        driver.back()
driver.close()
writeData(new)