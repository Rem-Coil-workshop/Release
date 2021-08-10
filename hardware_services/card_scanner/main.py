import json
import logging
import time
import traceback

import requests
import logger_config
from config import HEADERS, CARD_URL, SLEEP_TIME, MODE_DEV
from hardware_manipulation import listen_changes


def send_request(code: int):
    data = {'card': code}
    answer = requests.post(CARD_URL, data=json.dumps(data), headers=HEADERS)
    logging.info("Ответ сервера: " + str(answer.status_code))
    time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    logger_config.configure()
    logging.info("Сервис Card Scanner начал работу")
    while True:
        try:
            card_code = listen_changes()
            logging.info("Считано значение " + str(card_code))
            send_request(card_code)
        except Exception:
            logging.info("Ошибка соединения с сервером")
            if MODE_DEV:
                traceback.print_exc()
