from core.gpio_helper_hardware import GPIOHelper

slot_helper = None


def get_gpio_helper():
    global slot_helper
    if slot_helper is None:
        slot_helper = GPIOHelper()

    return slot_helper
