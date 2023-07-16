from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.chrome_executable_path="C:/Anthony/Selenium_20230709/day_7/chromedriver.exe"
driver = webdriver.Chrome(options=options)

driver.get('http://127.0.0.1/anthony/demo01.html')
eles = driver.find_elements(By.CLASS_NAME, "link")
for tag in eles:
    print(tag.text)
print(eles)

driver.close()