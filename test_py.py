import pytest
from selenium import webdriver
import time


def test_1(browser):
    link = "http://suninjuly.github.io/registration1.html"
    
    browser.get(link)
    input1=browser.find_element_by_css_selector('input.first[required]')
    input1.send_keys("joke")
    input2=browser.find_element_by_css_selector('input.second[required]')
    input2.send_keys("joke")
    input3=browser.find_element_by_css_selector('input.third[required]')
    input3.send_keys("joke")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text=="Congratulations! You have successfully registered!"

def test_2(browser):
    link = "http://suninjuly.github.io/registration2.html"
    
    browser.get(link)
    input1=browser.find_element_by_css_selector('input.first[required]')
    print(input1)
    input1.send_keys("joke")
    input2=browser.find_element_by_css_selector('input.second[required]')
    input2.send_keys("joke")
    input3=browser.find_element_by_css_selector('input.third[required]')
    input3.send_keys("joke")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text=="Congratulations! You have successfully registered!"

browser = webdriver.Chrome()
test_1(browser)
test_2(browser)
browser.quit()


