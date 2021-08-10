import RPi.GPIO as GPIO

from config import BUTTON_PIN


def set_up():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def listen_changes() -> bool:
    button_state = GPIO.input(BUTTON_PIN)
    return not button_state
