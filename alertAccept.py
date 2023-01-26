import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
browser.switch_to.alert.accept()

x = browser.find_element(By.ID, "input_value").text

input = browser.find_element(By.ID, "answer").send_keys(calc(x))
button = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

time.sleep(10)
browser.quit()