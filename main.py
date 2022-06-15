import warnings
import re
import array as arr
from fractions import Fraction
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
warnings.filterwarnings('ignore')

isdebug = False

i = 1
offset = 0

substring0 = "Thousandths"
substring1 = "Hundredths"
substring2 = "Tenths"

suparr = []
subarr = []
frac2decarr = []
fracresultarr = []
placevalarr = []
betweenarr = arr.array('f')
percentagesarr = []
dec2perarr = []
rawHCFarr = []
HCFarr = []
rawLCMarr = []
LCMarr = []
squaredarr = []
squarearr = []

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get("https://maths.prototec.co.nz/")

folder = driver.find_element_by_xpath("//input[@name='studentName']")
folder.click()
folder.send_keys("Leighton has no dad")
folder = driver.find_element_by_xpath("//input[@name='studentRoom']")
folder.click()
folder.send_keys("69")

print("Welcome to Prototec cheat(Made by GLUR). If there is any bugs please submit an issue in the github(github.com/GLUR-DEV/prototec)\n")
debug = input("Type 'debug' for debugging feedback. Or 'nodebug' for standard run\n")
while True:
    if debug == "debug":
        isdebug == True
        break
    elif debug == "nodebug":
        isdebug == False
        break
    else:
        print("'" + debug + "' is not a valid option\n")
        debug = input("Type 'debug' for debugging feedback. Or 'nodebug' for standard run\n")

Qdelay = input("Please enter delay between questions(in ms), keep in mind sheet takes 5 seconds to complete with 0 delay\n")
while True:
    if Qdelay.isdigit():
        Qdelay = int(Qdelay) / 1000
        break
    else:
        print("'" + Qdelay + "' is not a valid number")
        Qdelay = input("Please enter delay between questions(in ms), keep in mind sheet takes 5 seconds to complete with 0 delay\n")

input("Press any button to start solving(sheet and other stuff will be set automatically)")

folder = driver.find_element_by_xpath("//button[@value='s8']")
folder.click()

while i <= 20:
    folder = driver.find_element_by_xpath("(//sup)[" + str(i) + "]").text
    suparr.append(folder)
    i = i + 1

i = 1

while i <= 20:
    folder = driver.find_element_by_xpath("(//sub)[" + str(i) + "]").text
    subarr.append(folder)
    i = i + 1

i = 0

while i <= 7:
    xpathval = i + offset + 35
    folder = driver.find_element_by_xpath("(//td)[" + str(xpathval) + "]").text
    placevalarr.append(folder)
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
        finalfolder = finalfolder[0] + ".0" + finalfolder[1] + finalfolder[2] + finalfolder[3]

    finalfolder1 = finalfolder[0] + finalfolder[1] + finalfolder[2]
    finalfolder2 = finalfolder[3] + finalfolder[4] + finalfolder[5]
    betweenarr.append(float(finalfolder1))
    betweenarr.append(float(finalfolder2))
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

    percentagesarr.append(newfolder)
    i = i + 1
    offset = offset + 2

i = 0
offset = 0

while i < 5:
    xpathval = i + offset + 80
    folder = driver.find_element_by_xpath("(//td)[" + str(xpathval) + "]").text
    dec2perarr.append(folder)

    i = i + 1
    offset = offset + 2

i = 0
offset = 0

while i < 5:
    xpathval = i + offset + 95
    folder = driver.find_element_by_xpath("(//td)[" + str(xpathval) + "]").text
    rawHCFarr.append(folder)
    for word in folder.split():
        if word.isdigit():
            HCFarr.append(int(word))
    i = i + 1
    offset = offset + 2

i = 0
offset = 0

while i < 3:
    xpathval = i + offset + 107
    folder = driver.find_element_by_xpath("(//td)[" + str(xpathval) + "]").text
    rawLCMarr.append(folder)
    for word in folder.split():
        if word.isdigit():
            LCMarr.append(int(word))
    i = i + 1
    offset = offset + 2

i = 0
offset = 0

while i < 3:
    xpathval = i + offset + 116
    folder = driver.find_element_by_xpath("(//td)[" + str(xpathval) + "]").text
    newfolder = folder.replace(folder[-1], "")
    squaredarr.append(newfolder)
    square = ""
    for char in folder:
        if char == folder[-1]:
            square += char
    squarearr.append(square)
    i = i + 1
    offset = offset + 2

i = 0

if isdebug == True:
    print(suparr)
    print(subarr)
    print(frac2decarr)
    print(placevalarr)
    print(betweenarr)
    print(percentagesarr)
    print(dec2perarr)
    print(rawHCFarr)
    print(HCFarr)
    print(rawLCMarr)
    print(LCMarr)
    print(squaredarr)
    print(squarearr)

while i < 20:
    frac2decarr.append(int(suparr[i]) / int(subarr[i]))
    i = i + 1

i = 0
offset = 0

while i < 10:
    folder = driver.find_element_by_xpath("//input[@name='q" + str(i) + "']")

    if frac2decarr[i + offset] > frac2decarr[i + offset + 1]:
        folder.click()
        folder.send_keys(">")
        sleep(Qdelay)
    elif frac2decarr[i + offset] < frac2decarr[i + offset + 1]:
        folder.click()
        folder.send_keys("<")
        sleep(Qdelay)
    elif frac2decarr[i + offset] == frac2decarr[i + offset + 1]:
        folder.click()
        folder.send_keys("=")
        sleep(Qdelay)

    i = i + 1
    offset = offset + 1

i = 0

while i < 7:
    xpathval = i + 10
    folder = driver.find_element_by_xpath("//input[@name='q" + str(xpathval) + "']")

    if substring0 in placevalarr[i]:
        substringtype = 0
    elif substring1 in placevalarr[i]:
        substringtype = 1
    elif substring2 in placevalarr[i]:
        substringtype = 2

    if substringtype == 0:
        lastchar = placevalarr[i][-1]
        folder.click()
        folder.send_keys(lastchar)
        sleep(Qdelay)
    elif substringtype == 1:
        lastchar = placevalarr[i][-2]
        folder.click()
        folder.send_keys(lastchar)
        sleep(Qdelay)
    elif substringtype == 2:
        lastchar = placevalarr[i][-3]
        folder.click()
        folder.send_keys(lastchar)
        sleep(Qdelay)

    i = i + 1

i = 0
offset = 0

while i < 3:
    xpathval = i + 17
    folder = driver.find_element_by_xpath("//input[@name='q" + str(xpathval) + "']")
    result = (betweenarr[i + offset]) + (((betweenarr[i + offset + 1]) - (betweenarr[i + offset])) / 2)
    folder.click()
    folder.send_keys(round(result, 2))
    sleep(Qdelay)

    i = i + 1
    offset = offset + 1

i = 0

while i < 5:
    xpathval = i + 20
    folder = driver.find_element_by_xpath("//input[@name='q" + str(xpathval) + "']")
    reducefrac = Fraction(int(percentagesarr[i]), 100)
    folder.click()
    folder.send_keys(str(reducefrac))
    sleep(Qdelay)
    i = i + 1

i = 0

while i < 5:
    xpathval = i + 25
    folder = driver.find_element_by_xpath("//input[@name='q" + str(xpathval) + "']")
    dec2perresult = float(dec2perarr[i]) * 100
    folder.click()
    folder.send_keys(round(dec2perresult))
    sleep(Qdelay)
    i = i + 1

i = 0
offset = 0

while i < 4:
    xpathval = i + 30
    folder = driver.find_element_by_xpath("//input[@name='q" + str(xpathval) + "']")

    if HCFarr[i + offset] > HCFarr[i + offset + 1]:
            smaller = HCFarr[i + offset + 1]
    else:
            smaller = HCFarr[i + offset]
    for ii in range(1, smaller+1):
        if((HCFarr[i + offset] % ii == 0) and (HCFarr[i + offset + 1] % ii == 0)):
             hcf = ii
    folder.click()
    folder.send_keys(hcf)
    sleep(Qdelay)

    i = i + 1
    offset = offset + 1

i = 0
ii = 0
offset = 0
lcm = 0

while i < 3:
    xpathval = i + 34
    folder = driver.find_element_by_xpath("//input[@name='q" + str(xpathval) + "']")

    if LCMarr[i + offset] > LCMarr[i + offset + 1]:
            greater = LCMarr[i + offset]
    else:
            greater = LCMarr[i + offset + 1]
    while (True):
        if ((greater % LCMarr[i + offset] == 0) and (greater % LCMarr[i + offset + 1] == 0)):
            lcm = greater
            break
        greater += 1
    folder.click()
    folder.send_keys(lcm)
    sleep(Qdelay)

    i = i + 1
    offset = offset + 1

i = 0

while i < 3:
    xpathval = i + 37
    folder = driver.find_element_by_xpath("//input[@name='q" + str(xpathval) + "']")
    result = int(squaredarr[i])**int(squarearr[i])
    folder.click()
    folder.send_keys(result)
    sleep(Qdelay)
    i = i + 1

input("Process complete! Press mark.")
