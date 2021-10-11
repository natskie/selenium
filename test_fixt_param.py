from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num', ["236895", "236896","236897","236898","236899","236903","236904","236905"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, num):
        browser.get("https://stepik.org/lesson/"+num+"/step/1")
        browser.implicitly_wait(5)
        ta=browser.find_element_by_css_selector('textarea.string-quiz__textarea')
        answer = math.log(int(time.time()))
        ta.send_keys(str(answer))
        bt= browser.find_element_by_css_selector('button.submit-submission')
        bt.click()
        res=browser.find_element_by_css_selector('pre.smart-hints__hint')
        if  res.text!="Correct!":
            print(res.text)


#browser.quit()

