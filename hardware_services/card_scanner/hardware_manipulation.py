import serial
import logging
from config import PORT, FREQUENCY, MODE_DEV


def listen_changes() -> int:
    with serial.Serial(PORT, FREQUENCY) as card:
        data = b''
        current_byte = b''
        while current_byte != b'\x03':
            if MODE_DEV:
                logging.info(b'Value: ' + current_byte)
            if current_byte != b'\x02':
                data += current_byte
            current_byte = card.read()

    if MODE_DEV:
        logging.info(b'Value: ' + data)

    return int(data[2:-2], 16)
