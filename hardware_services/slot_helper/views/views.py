from flask import request

from app import app
from core.resourse_helper import get_slot_helper


@app.route('/open_slot', methods=['POST'])
def boxes():
    content = request.json
    box_number = content["box"]
    slot_helper = get_slot_helper()
    app.logger.info("Ячейка " + str(box_number) + " открыта")
    slot_helper.open_slot(box_number)
    return 'success'
