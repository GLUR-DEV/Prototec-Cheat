import requests
import re
import array as arr
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import warnings
warnings.filterwarnings('ignore')

i = 1
offset = 0
num = 0

substring0 = "Thousandths"
substring1 = "Hundredths"
substring2 = "Tenths"

sup = []
sub = []
frac2dec = []
fracresult = []
placeval = []
between = arr.array('f')
percentages = []

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

while i <= 7:
    xpathval = i + offset + 35
    folder = driver.find_element_by_xpath("(//td)[" + str(xpathval) + "]").text
    placeval.append(folder)
    i = i + 1
    offset = offset + 2

i = 0
offset = 0

while i < 3:
    xpathval = i + offset + 56
    folder = driver.find_element_by_xpath("(//td)[" + str(xpathval) + "]").text
    newfolder = re.findall('\d*\.?', folder)
    finalfolder = ""
    for char in newfolder:
        if char != "[":
            finalfolder += char
    if finalfolder[-3] == ".":
        finalfolder = finalfolder + ".0"
    elif finalfolder[2] == ".":
        finalfolder = finalfolder[0] + ".0" + finalfolder[1]+finalfolder[2]+finalfolder[3]

    finalfolder1 = finalfolder[0]+finalfolder[1]+finalfolder[2]
    finalfolder2 = finalfolder[3]+finalfolder[4]+finalfolder[5]
    between.append(float(finalfolder1))
    between.append(float(finalfolder2))
    i = i + 1
    offset = offset + 2

i = 0
offset = 0

while i < 5:
    xpathval = i + offset + 65
    folder = driver.find_element_by_xpath("(//td)[" + str(xpathval) + "]").text
    newfolder = ""
    for char in folder:
        if char != "%":
            newfolder += char

    percentages.append(newfolder)
    i = i + 1
    offset = offset + 2

i = 0
offset = 0

while i < 20:
    frac2dec.append(int(sup[i]) / int(sub[i]))
    i = i + 1

i = 0
offset = 0

print(sup)
print(sub)
print(frac2dec)
print(placeval)
print(between)
print(percentages)

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

while i < 7:
    xpathval = i + 10
    folder = driver.find_element_by_xpath("//input[@name='q" + str(xpathval) + "']")

    if substring0 in placeval[i]:
        substringtype = 0
    elif substring1 in placeval[i]:
        substringtype = 1
    elif substring2 in placeval[i]:
        substringtype = 2

    if substringtype == 0:
        lastchar = placeval[i][-1]
        folder.click()
        folder.send_keys(lastchar)
    elif substringtype == 1:
        lastchar = placeval[i][-2]
        folder.click()
        folder.send_keys(lastchar)
    elif substringtype == 2:
        lastchar = placeval[i][-3]
        folder.click()
        folder.send_keys(lastchar)

    i = i + 1

i = 0
offset = 0

while i < 3:
    xpathval = i + 17
    folder = driver.find_element_by_xpath("//input[@name='q" + str(xpathval) + "']")
    result = (between[i+offset]) + (((between[i+offset+1]) - (between[i+offset])) / 2)
    folder.click()
    folder.send_keys(round(result, 2))

    i = i + 1
    offset = offset + 1

sleep(100)
