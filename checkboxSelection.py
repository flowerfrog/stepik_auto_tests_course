from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "div.form-group > input[required]")
    input.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
