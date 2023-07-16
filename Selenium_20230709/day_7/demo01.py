from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.chrome_executable_path="C:/Anthony/Selenium_20230709/day_7/chromedriver.exe"
driver = webdriver.Chrome(options=options)

driver.get('http://127.0.0.1/anthony/demo01.html')
# eles = driver.find_elements(By.CLASS_NAME, "link")
# for tag in eles:
#     print(tag.text)
# print(eles)

el_3 = driver.find_element(By.CLASS_NAME, "link-3")
print("/el_3 : "+el_3.text)
el_3_text = el_3.find_element(By.TAG_NAME, 'p')
print("/el_3_text : "+el_3_text.text)

el_4 = driver.find_element(By.CLASS_NAME, "link-4")
el_4.click()

time.sleep(3)

driver.close()