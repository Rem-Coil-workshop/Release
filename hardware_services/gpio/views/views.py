from app import app
from core.resourse_helper import get_gpio_helper


@app.route('/turn_card')
def turn_card():
    slot_helper = get_gpio_helper()
    slot_helper.card_turn_on()
    return 'success'


@app.route('/turn_qr')
def turn_qr():
    slot_helper = get_gpio_helper()
    slot_helper.qr_turn_on()
    return 'success'


@app.route('/turn_off')
def turn_off():
    slot_helper = get_gpio_helper()
    slot_helper.turn_off_all()
    return 'success'
