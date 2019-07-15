import logging
import time
from datetime import datetime


def get_logger(name: str):
    """
    ハンドラ設定をしたloggerオブジェクトを返却する。
    :param name: 実行ファイルのname要素
    :return: loggerオブジェクト
    """
    logger = logging.getLogger(name)

    # logレベル設定
    logger.setLevel(logging.DEBUG)

    # ログ出力フォーマット設定
    handler_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # log出力先設定
    file_handler = logging.FileHandler('/log/pylog/py.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(handler_format)

    # 標準出力設定
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(handler_format)

    # Handlerをセット
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


def stop_watch(message: str, logger):
    """
    時間計測デコレーター
    :param message: 任意のメッセージ
    :param logger: loggerオブジェクト
    """

    def _stop_watch(func):
        def wrapper(*args, **kargs):
            start = time.time()
            logger.info(datetime.now())
            result = func(*args, **kargs)
            elapsed_time = time.time() - start
            logger.info(f"{message}は{elapsed_time}秒かかりました")
            return result

        return wrapper

    return _stop_watch
