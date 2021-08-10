import json
import logging
import time
import traceback

import requests
import logger_config
from config import QR_URL, HEADERS, SLEEP_TIME, MODE_DEV
from hardware_manipulation import listen_changes, set_up


def send_request(qr_code: str):
    data = {'qr': qr_code}
    answer = requests.post(QR_URL, data=json.dumps(data), headers=HEADERS)
    logging.info("Ответ сервера: " + str(answer.status_code))
    time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    set_up()
    logger_config.configure()
    logging.info("Сервис Qr Scanner начал работу")
    while True:
        try:
            qr = listen_changes()
            logging.info("Считано значение " + str(qr))
            send_request(qr)
        except Exception:
            logging.info("Ошибка соединения с сервером")
            if MODE_DEV:
                traceback.print_exc()
