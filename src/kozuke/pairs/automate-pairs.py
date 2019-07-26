"""
アプリの足跡自動化ツール
元ネタ
https://rikediary.com/matching-app/automation/python-pairs/
"""
from os import environ
from os.path import basename
import time
import random
import re

from selenium import webdriver

from commonlib.log import get_logger, stop_watch

_PAIRS_LOGIN_URL = 'https://pairs.lv/#/login'
_SEARCH_RESULT_COUNT_SELECTOR = '#pairs_search_page > div > div.box_search_menu > p:nth-child(5)'
_FACE_BOOK_LOGIN_BUTTON = '#registerBtn1'
_FIRST_ACCESS_NUM = 1
_MAX_ACCESS_NUM_BASE = int(environ['PAIRS_MAX_ACCESS_NUM'])
_ADD_ACCESS_NUM = int(environ['PAIRS_ADD_ACCESS_NUM'])
_PROFILE_PATH = r'/Users/kota-ishizuka/Library/Application Support/Google/Chrome'
fail_count = 0

# logger
logger = get_logger(__name__)


@stop_watch(basename(__file__), logger)
def main():
    current_access_count = 0

    max_access_num = random.randint(_MAX_ACCESS_NUM_BASE, _MAX_ACCESS_NUM_BASE + _ADD_ACCESS_NUM)
    options = webdriver.ChromeOptions()
    # options.add_argument("user-data-dir=" + _PROFILE_PATH) # これでsession保てるはずだができない。

    # このprofileを読み込ませることで「facebook.comが許可を求めています。」のアラートがなくなる。
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(_PAIRS_LOGIN_URL)
    time.sleep(5)
    authenticate_facebook(driver)

    src = "https://pairs.lv/#/search/one/%s" % str(_FIRST_ACCESS_NUM)
    driver.get(src)
    num_list = get_random_list(driver)
    time.sleep(5)

    logger.info(f'max_access_num:{max_access_num}')
    for i, num in enumerate(num_list, start=1):
        if current_access_count >= max_access_num:
            break
        current_access_count = current_access_count + 1
        src = "https://pairs.lv/#/search/one/%s" % str(num)
        try:
            driver.get(src)
        except Exception as e:
            continue
        logger.info(f'{i}人目：{num}')
        time.sleep(random.randint(7, 9))

    logger.info(f"{current_access_count}人に足跡を付けました")
    driver.close()
    driver.quit()


def authenticate_facebook(driver):
    """
    Facebookアカウントからログイン認証を行う。
    :param driver: chrome driver
    """
    driver.find_element_by_css_selector(_FACE_BOOK_LOGIN_BUTTON).click()

    time.sleep(5)
    handle_array = driver.window_handles
    driver.switch_to.window(handle_array[1])
    driver.find_element_by_css_selector('#email').send_keys(environ['FACEBOOK_EMAIL'])
    driver.find_element_by_css_selector('#pass').send_keys(environ['FACEBOOK_PASS'])
    try:
        driver.find_element_by_css_selector('#u_0_0').click()
        time.sleep(5)
        driver.switch_to.window(handle_array[0])
    except:
        # "We could not log you in"が出た時の逃げ対応
        time.sleep(3)
        driver.find_element_by_css_selector('#u_0_2').click()
        time.sleep(5)
        driver.close()
        time.sleep(3)
        driver.switch_to.window(handle_array[0])
        time.sleep(5)
        driver.find_element_by_css_selector(_FACE_BOOK_LOGIN_BUTTON).click()
        time.sleep(5)


def get_random_list(driver):
    """
    検索結果の件数を取得し、件数分のリストを作成する。
    そのリストをシャッフルして返却する。（ランダムに足跡をつけるため。）

    たまにCSSセレクタを取得できない場合があるので、10回まで再帰処理で繰り返す。
    10回処理をしても取得できない場合は、処理を強制終了する。
    :param driver: chrome driver
    :return: 検索結果の件数分のシャッフルした数値リスト
    """
    try:
        global fail_count
        time.sleep(1)
        result_count_info = driver.find_element_by_css_selector(_SEARCH_RESULT_COUNT_SELECTOR).text
        result_count = int(re.search(r'^\d+', re.sub(',', '', result_count_info)).group(0))
        logger.info(f'result_count: {result_count}')
        if result_count == 0:
            exit(1)
        num_list = list(range(1, result_count))
        random.shuffle(num_list)
        return num_list
    except Exception as e:
        if fail_count >= 10:
            logger.error('css NG')
            return exit(1)
        fail_count += 1
        time.sleep(3)
        return get_random_list(driver)


if __name__ == '__main__':
    main()
