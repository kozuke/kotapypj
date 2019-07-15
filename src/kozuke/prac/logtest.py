import logging
from os.path import basename

from commonlib.log import stop_watch

logger = logging.getLogger(__name__)
get_handler = logging.FileHandler('logfile/logger.log')
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()

# handlerのログレベル設定(ハンドラが出力するエラーメッセージのレベル)
stream_handler.setLevel(logging.DEBUG)

# ログ出力フォーマット設定
handler_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(handler_format)
get_handler.setFormatter(handler_format)

logger.addHandler(stream_handler)
logger.addHandler(get_handler)


@stop_watch(basename(__file__), logger)
def main():
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.fatal('fatal')


if __name__ == '__main__':
    main()
