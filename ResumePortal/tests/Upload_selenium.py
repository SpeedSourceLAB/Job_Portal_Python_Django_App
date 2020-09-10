from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.firefox import GeckoDriverManager

#firefox_driver= webdriver.Firefox(executable_path="C:\\Users\\prade\\Downloads\\geckodriver-v0.27.0-win64\\geckodriver.exe")
firefox_driver= webdriver.Chrome(executable_path="C:\\Users\\prade\\PycharmProjects\\webdrivers\\chromedriver_win32\\chromedriver.exe")
#firefox_driver= webdriver.Firefox(executable_path=GeckoDriverManager().install())
#firefox_driver.get("https://www.google.com")
firefox_driver.get("http://127.0.0.1:8000/")
firefox_driver.maximize_window()
print(firefox_driver.title)
print(firefox_driver.current_url)
time.sleep(5)
#chrome_driver.find_element_by_id("txt").clear()
time.sleep(5)
#chrome_driver.find_element_by_id("txt").send_keys("C:\\Users\\prade\\Downloads\\Sample_Resume_Format.docx")
#chrome_driver.find_element_by_id("txt").send_keys("C:\\Users\\prade\\Downloads\\Table_Resume_Format.docx")
firefox_driver.find_element_by_name("file1").send_keys("C:\\Users\\prade\\Downloads\\Table_Resume_Format.docx")

time.sleep(5)
firefox_driver.find_element_by_id("upload").click()
time.sleep(5)
firefox_driver.find_element_by_id("Subtn").click()
time.sleep(5)
firefox_driver.find_element_by_id("backToHome").click()
time.sleep(5)
firefox_driver.close()