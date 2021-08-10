from datetime import datetime
from smbus import SMBus
from app import app
from app.config import KEY_CONTROLLER_ADDRESS


class SlotHelper:
    last_open = datetime(1970, 1, 1)

    def open_slot(self, slot_number: int):
        now = datetime.now()

        if (now - self.last_open).seconds > 5:
            self.last_open = now
            self._open_slot(slot_number)

    @staticmethod
    def _open_slot(slot_number: int):
        bus = SMBus(1)
        app.logger.info(slot_number)
        bus.write_byte(KEY_CONTROLLER_ADDRESS, slot_number)
        app.logger.info("close connection i2c")
        bus.close()
