from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.chrome_executable_path="C:/Anthony/Selenium_20230709/day_7/chromedriver.exe"
driver = webdriver.Chrome(options=options)

driver.get('https://www.linkedin.com/jobs/search?trk=content-hub-home-page_guest_nav_menu_jobs&position=1&pageNum=0')

# title = driver.find_element(By.CLASS_NAME, 'base-card').find_element(By.CLASS_NAME, "base-search-card__info").find_element(By.CLASS_NAME, "base-search-card__title")
# print(title.text)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    


driver.close()