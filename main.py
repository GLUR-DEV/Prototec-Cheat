import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import warnings

warnings.filterwarnings('ignore')

sup = []
sub = []

options = Options()
# options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get("https://maths.prototec.co.nz/")

folder = driver.find_element_by_xpath("//button[@value='s8']")
folder.click()

folder = driver.find_element_by_xpath("(//sup)[1]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[2]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[3]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[4]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[5]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[6]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[7]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[8]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[9]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[10]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[11]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[12]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[13]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[14]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[15]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[16]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[17]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[18]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[19]").text
sup.append(folder)
folder = driver.find_element_by_xpath("(//sup)[20]").text
sup.append(folder)

folder = driver.find_element_by_xpath("(//sub)[1]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[2]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[3]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[4]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[5]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[6]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[7]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[8]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[9]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[10]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[11]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[12]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[13]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[14]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[15]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[16]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[17]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[18]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[19]").text
sub.append(folder)
folder = driver.find_element_by_xpath("(//sub)[20]").text
sub.append(folder)



#print(sup)
#print(sub)
sleep(100)


