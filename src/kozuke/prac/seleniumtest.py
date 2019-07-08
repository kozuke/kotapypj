import time

from selenium import webdriver

PAIRS_LOGIN_URL = 'https://pairs.lv/#/login'
FACE_BOOK_LOGIN_BUTTON = '#registerBtn1'


def main():
    driver = webdriver.Chrome()
    driver.get(PAIRS_LOGIN_URL)
    print(driver.current_url)
    time.sleep(5)
    driver.find_element_by_css_selector(FACE_BOOK_LOGIN_BUTTON).click()
    time.sleep(5)
    handle_array = driver.window_handles
    driver.switch_to.window(handle_array[1])
    print(driver.current_url)
    driver.find_element_by_css_selector('#email').send_keys('')
    driver.find_element_by_css_selector('#pass').send_keys('')
    driver.find_element_by_css_selector('#u_0_0').click()
    time.sleep(5)
    driver.switch_to.window(handle_array[0])
    print(driver.current_url)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    main()
