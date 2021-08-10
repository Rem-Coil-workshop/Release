from core.slot_helper_hardware import SlotHelper

slot_helper = None


def get_slot_helper():
    global slot_helper
    if slot_helper is None:
        slot_helper = SlotHelper()

    return slot_helper
