# Работа с лапочками
Данный сервис слушает запросы по определенному порту и включает/выключает лапочки по запросу
### Конфигурация
В файле конфигурации прописывается порт, на котором поднят сервис и порты лампочек:
```python
PORT = 3000  
  
CARD_LED_PIN = 16  
QR_LED_PIN = 18
```
### Обработка запросов
Для каждого действия прописаны свои конечные точки:
```python
@app.route('/turn_card')  
def turn_card():  
    # body
  
@app.route('/turn_qr')  
def turn_qr():  
    # body 
  
  
@app.route('/turn_off')  
def turn_off():  
    # body
```
### Включение/выключение лампочек
За включение/выключение отвечает класс GPIOHelper. В методе *init* выполняется указание портов.

Далее описываются методы, которые логируют операцию и вызывают определённый статический метод с необходимыми параметрами.
```python
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
```