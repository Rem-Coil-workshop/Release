import logging

import evdev
from config import PORT, MODE_DEV

scancodes = {
    2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8', 10: u'9', 11: u'0', 12: u'-', 16: u'Q',
    17: u'W', 18: u'E', 19: u'R', 20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 30: u'A', 31: u'S',
    32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 44: u'Z', 45: u'X', 46: u'C', 47: u'V',
    48: u'B', 49: u'N', 50: u'M', 53: u'/', 54: u'RSHFT', 57: u' '
}

device = None


def set_up():
    global device
    device = evdev.InputDevice(PORT)


# noinspection PyUnresolvedReferences
def listen_changes() -> str:
    global device
    code = []
    data = ""
    is_upper = True

    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY and event.value == 1:
            e_code = event.code
            if MODE_DEV:
                logging.info('Считано значение: ' + str(e_code))
            if e_code == 28:
                data = data.join(code)
                break
            elif e_code == 54:
                is_upper = False
            elif 16 <= e_code <= 50:
                word = scancodes[e_code] if is_upper else scancodes[e_code].lower()
                code.append(word)
                is_upper = True
            elif 2 <= e_code <= 11 or e_code == 53 or e_code == 12 or e_code == 57:
                code.append(scancodes[e_code])

    return data
