# Сервис открытия ячейки
Данный сервис слушает запросы POST на '/open_slot', получает из тела запроса номер ячейки и передаёт это значение в необходимый класс:
```kotlin
@app.route('/open_slot', methods=['POST'])  
def boxes():  
    content = request.json  
    box_number = content["box"]  
    slot_helper = get_slot_helper()  
    slot_helper.open_slot(box_number)  
    return 'success'
```
### Открытие ячейки
Для открытия ячейки используется библиотека `smbus`. Контроллеры, которые открывают ячейки, подключены к мастеру по I2C. При получении номера ячейки, класс отправляет по адресу контроллера полученное значение ячейки:
```python
@staticmethod  
def _open_slot(slot_number: int):  
    bus = SMBus(1)  
    bus.write_byte(KEY_CONTROLLER_ADDRESS, slot_number)  
    bus.close()
```
### Конфигурация
В файле конфигурации указывается порт, на котором поднят сервис, и адрес контроллера:
```python
PORT = 2000  
  
KEY_CONTROLLER_ADDRESS = 0x8
```