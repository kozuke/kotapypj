"""
Pairsの足跡自動化ツール
元ネタ
https://rikediary.com/matching-app/automation/python-pairs/
"""
import time
import random
import re
from functools import wraps

from selenium import webdriver

PAIRS_LOGIN_URL = 'https://pairs.lv/#/login'
SEARCH_RESULT_COUNT_SELECTOR = '#pairs_search_page > div > div.box_search_menu > p:nth-child(5)'
FIRST_ACCESS_NUM = 1
fail_cnt = 0


def stop_watch(func):
    """
    時間計測デコレーター
    TODO to-be ライブラリ化
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{func.__name__}は{elapsed_time}秒かかりました")
        return result

    return wrapper


@stop_watch
def main():
    current_access_count = 0
    max_access_num_base = 145
    max_access_num = random.randint(max_access_num_base, max_access_num_base + 30)
    driver = webdriver.Chrome()
    driver.get(PAIRS_LOGIN_URL)
    time.sleep(5)

    key = input('ログイン後、pairsのトップページが出たらyを押してください>>')
    if key == 'y':
        src = "https://pairs.lv/#/search/one/%s" % str(FIRST_ACCESS_NUM)
        driver.get(src)
        num_list = get_random_list(driver)
        time.sleep(random.randint(4, 8))
    else:
        return
    print('max_access_num:', max_access_num)
    for num in num_list:
        if current_access_count >= max_access_num:
            break
        current_access_count = current_access_count + 1
        src = "https://pairs.lv/#/search/one/%s" % str(num)
        try:
            driver.get(src)
        except:
            continue
        print(str(num))
        time.sleep(random.randint(8, 13))

    print(f"{current_access_count}人に足跡を付けました")
    driver.close()
    driver.quit()


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
        global fail_cnt
        time.sleep(1)
        result_count_info = driver.find_element_by_css_selector(SEARCH_RESULT_COUNT_SELECTOR).text
        result_count = int(re.search(r'^\d+', re.sub(',', '', result_count_info)).group(0))
        print('result_count:', result_count)
        if result_count == 0:
            exit(1)
        num_list = list(range(1, result_count))
        random.shuffle(num_list)
        return num_list
    except Exception as e:
        if fail_cnt >= 10:
            print('css NG')
            return exit(1)
        fail_cnt += 1
        return get_random_list(driver)


if __name__ == '__main__':
    main()
