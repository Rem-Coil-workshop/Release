from app import app


class GPIOHelper:
    def qr_turn_on(self):
        app.logger.info("Turn qr led")

    def card_turn_on(self):
        app.logger.info("Turn card led")

    def qr_turn_off(self):
        app.logger.info("Turn off qr led")

    def card_turn_off(self):
        app.logger.info("Turn off card led")

    def turn_off_all(self):
        self.card_turn_off()
        self.qr_turn_off()
