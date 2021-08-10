import logging
import time

import requests
import logger_config
from config import BUTTON_URL, SLEEP_TIME
from hardware_manipulation import listen_changes, set_up


def send_request():
    answer = requests.get(BUTTON_URL)
    logging.info("Ответ сервера: " + str(answer.status_code))
    time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    set_up()
    logger_config.configure()
    logging.info("Сервис Button начал работу")
    while True:
        try:
            if listen_changes():
                logging.info("Нажали кнопку")
                send_request()
        except Exception:
            logging.info("Ошибка соединения с сервером")
