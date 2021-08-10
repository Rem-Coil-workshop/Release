import RPi.GPIO as GPIO
from app import app
from app.config import QR_LED_PIN, CARD_LED_PIN


class GPIOHelper:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(QR_LED_PIN, GPIO.OUT)
        GPIO.setup(CARD_LED_PIN, GPIO.OUT)

    def qr_turn_on(self):
        app.logger.info("Turn qr led")
        self._turn_led(QR_LED_PIN, True)

    def card_turn_on(self):
        app.logger.info("Turn card led")
        self._turn_led(CARD_LED_PIN, True)

    def qr_turn_off(self):
        app.logger.info("Turn off qr led")
        self._turn_led(QR_LED_PIN, False)

    def card_turn_off(self):
        app.logger.info("Turn off card led")
        self._turn_led(CARD_LED_PIN, False)

    def turn_off_all(self):
        self.card_turn_off()
        self.qr_turn_off()

    @staticmethod
    def _turn_led(led_pin: int, is_turn: bool):
        if is_turn:
            mode = GPIO.HIGH
        else:
            mode = GPIO.LOW

        GPIO.output(led_pin, mode)
