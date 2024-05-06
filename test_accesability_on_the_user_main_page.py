from selenium import webdriver
from selenium.webdriver.common.by import By
class TestAccesability:
    def test_check_quantity_links(self):
        url = 'http://metro-mo.ru'
        with webdriver.Chrome() as browser:
            browser.get(url)
            Login = browser.find_element(By.XPATH, "//input[@name='login']")
            Password = browser.find_element(By.XPATH, "//input[@name='pass']")
            Login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
            Login.send_keys('qa_best_test')
            Password.send_keys('learnqa')
            Login_button.click()
            links_on_this_page = browser.find_elements(By.TAG_NAME, 'a')
            expected_result = 6
            actual_result = len(links_on_this_page)
            assert actual_result == expected_result, "actual_result doesn't look like expected_result"
    def test_check_quantity_paragrafs(self):
        url = 'http://metro-mo.ru'
        with webdriver.Chrome() as browser:
            browser.get(url)
            Login = browser.find_element(By.XPATH, "//input[@name='login']")
            Password = browser.find_element(By.XPATH, "//input[@name='pass']")
            Login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
            Login.send_keys('qa_best_test')
            Password.send_keys('learnqa')
            Login_button.click()
            paragrafs_on_this_page = browser.find_elements(By.TAG_NAME, 'p')
            expected_result = 0
            actual_result = len(paragrafs_on_this_page)
            assert actual_result == expected_result, "actual_result doesn't look like expected_result"
    def test_check_quantity_headers(self):
        url = 'http://metro-mo.ru'
        with webdriver.Chrome() as browser:
            browser.get(url)
            Login = browser.find_element(By.XPATH, "//input[@name='login']")
            Password = browser.find_element(By.XPATH, "//input[@name='pass']")
            Login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
            Login.send_keys('qa_best_test')
            Password.send_keys('learnqa')
            Login_button.click()
            headers_on_this_page = browser.find_elements(By.TAG_NAME, 'h2')
            expected_result = 0
            actual_result = len(headers_on_this_page)
            assert actual_result == expected_result, "actual_result doesn't look like expected_result"