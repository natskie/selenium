from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
tit = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), "$100"))
button=browser.find_element_by_css_selector('button#book')
button.click()
num=int(browser.find_element_by_css_selector('span#input_value').text)
num1=math.log(abs(12*math.sin(num)))
tex=browser.find_element_by_css_selector('input#answer')
tex.send_keys(str(num1))
button=browser.find_element_by_css_selector('button#solve')
button.click()