import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import warnings

warnings.filterwarnings('ignore')

substring0 = "Thousandths"
substring1 = "Hundredths"
substring2 = "Tenths"

i = 1
placevaltype = 0
offset = 0

sup = []
sub = []
frac2dec = []
fracresult = []

options = Options()
# options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get("https://maths.prototec.co.nz/")

folder = driver.find_element_by_xpath("//button[@value='s8']")
folder.click()

while i <= 20:
    folder = driver.find_element_by_xpath("(//sup)[" + str(i) + "]").text
    sup.append(folder)
    i = i + 1

i = 1

while i <= 20:
    folder = driver.find_element_by_xpath("(//sub)[" + str(i) + "]").text
    sub.append(folder)
    i = i + 1

i = 0

while i <= 20:
    folder = driver.find_element_by_xpath("(//td)[" + i + offset + 35 + "]").text

print(sup)
print(sub)

while i < 20:
    frac2dec.append(int(sup[i]) / int(sub[i]))
    i = i + 1

print(frac2dec)
i = 0
offset = 0

while i < 10:
   folder = driver.find_element_by_xpath("//input[@name='q" + str(i) + "']")

   if frac2dec[i+offset] > frac2dec[i+offset+1]:
       folder.click()
       folder.send_keys(">")
   elif frac2dec[i+offset] < frac2dec[i+offset+1]:
       folder.click()
       folder.send_keys("<")
   elif frac2dec[i+offset] == frac2dec[i+offset+1]:
       folder.click()
       folder.send_keys("=")

   i = i + 1
   offset = offset + 1

i = 0

while i < 10:
    if substring0 in

sleep(100)






