import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.maximize_window()

# Display cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:", cookies_before_login)

username=driver.find_element(By.ID,"user-name")
time.sleep(2)
username.click()
time.sleep(2)
username.send_keys("standard_user")
passw=driver.find_element(By.ID,"password")
passw.click()
passw.send_keys("secret_sauce")
logins=driver.find_element(By.ID,"login-button")
logins.click()

# Display cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:", cookies_after_login)

time.sleep(2)
driver.close()


