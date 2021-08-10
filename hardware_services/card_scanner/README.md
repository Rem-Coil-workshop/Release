# Работа с картами
Для работы с картами используется библиотека `serial`. Для считывания открывается стрим на необходимом порте.

При поступлении данных в стрим, функция считывает битовые символы до символа окончания строки (`b'\x03'`), далее убирает системные биты и возвращает считанное значение:
```python
def listen_changes() -> int:  
    with serial.Serial(PORT, FREQUENCY) as card:  
        data = b''  
 		current_byte = b''  
 		while current_byte != b'\x03':
            if current_byte != b'\x02':  
                data += current_byte  
            current_byte = card.read()  
  
    return int(data[2:-2], 16)
```
После успешного считывания, сервис формирует json и отправляет его методом POST в главный сервис.
```python
def send_request(code: int):  
    data = {'card': code}  
    answer = requests.post(CARD_URL, data=json.dumps(data), headers=HEADERS)
```
### Конфигурация
В файле конфигурации прописывается конечная точка, куда отправляется запрос и порт сканера (и частота опроса сканера):
```python
CARD_URL = 'http://127.0.0.1:80/v1/slots/card'  
HEADERS = {'Content-Type': 'application/json'}  
  
PORT = '/dev/serial0'  
FREQUENCY = 9600  
```