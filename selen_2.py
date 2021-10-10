from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    
    browser.get(link)
    button = browser.find_element_by_css_selector('button.btn-primary')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    n=int(browser.find_element_by_css_selector('span#input_value').text)
    num=math.log(abs(12*math.sin(n)))
    browser.find_element_by_css_selector('input#answer').send_keys(str(num))
    button = browser.find_element_by_css_selector('button.btn-primary')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    
    browser.quit()


