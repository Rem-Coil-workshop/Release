from datetime import datetime


class SlotHelper:
    last_open = datetime(1970, 1, 1)

    def open_slot(self, slot_number: int):
        now = datetime.now()

        if (now - self.last_open).seconds > 5:
            self.last_open = now
