import logging

import evdev
from config import PORT, MODE_DEV

device = None


def set_up():
    global device
    device = evdev.InputDevice(PORT)


def listen_changes() -> str:
    global device
    code = []
    data = ""

    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY and event.value == 1:
            e_code = event.code - 1
            if MODE_DEV:
                logging.info('Считано значение: ' + str(e_code))
            if 1 <= e_code <= 10:
                digit = str(0)
                if e_code != 10:
                    digit = str(e_code)
                code.append(digit)
            elif e_code == 52:
                code.append('/')
            elif e_code == 11:
                code.append('-')
            elif e_code == 27:
                data = data.join(code)
                break

    return data
