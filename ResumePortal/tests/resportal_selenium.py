from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#import autoit
#from autoit import *

#ie_driver= webdriver.Edge(executable_path="C:\\Users\\prade\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe")
#chrome_driver= webdriver.Firefox(executable_path="C:\\Users\\prade\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe")

chrome_driver= webdriver.Chrome(executable_path="C:\\Users\\prade\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
chrome_driver.get("http://127.0.0.1:8000/")
chrome_driver.maximize_window()
print(chrome_driver.title)
print(chrome_driver.current_url)
time.sleep(5)
#chrome_driver.find_element_by_id("txt").clear()
#chrome_driver.find_element_by_id("txt").send_keys("C:\\Users\\prade\\Downloads\\Sample_Resume_Format.docx")

#chrome_driver.find_element_by_name("file1").send_keys("C:\\Users\\prade\\Downloads\\Table_Resume_Format.docx")
"""
chrome_driver.find_element_by_id("txt").click()
#chrome_driver.implicitly_wait(5)
time.sleep(5)

control_focus("Open","Edit1")
control_set_text("Open","Edit1","C:\\Users\\prade\\Downloads\\Table_Resume_Format.docx")
control_click("Open","Button1")
time.sleep(5)
chrome_driver.find_element_by_id("upload").click()
time.sleep(5)
chrome_driver.find_element_by_id("Subtn").click()
time.sleep(5)
chrome_driver.find_element_by_id("backToHome").click()
time.sleep(5)
"""

fileww= chrome_driver.find_element_by_name("file1")
fileww.send_keys("C:\\Users\\prade\\Downloads\\Table_Resume_Format.docx")
time.sleep(5)
chrome_driver.find_element_by_id("upload").click()
time.sleep(5)
chrome_driver.find_element_by_id("Subtn").click()
time.sleep(5)
chrome_driver.find_element_by_id("backToHome").click()
time.sleep(5)

chrome_driver.close()