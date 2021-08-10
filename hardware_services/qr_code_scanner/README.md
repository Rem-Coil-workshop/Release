# Работа с qr кодами
Для работы с кодами используется библиотека `evdev`. С её помощью открывает необходимое устройство и считывается значения с него.

При поступлении данных в стрим, функция сохраняет известные коды символов. Если введён символ окончания строки (`27`), функция возвращает значение:
```python
def listen_changes() -> str:  
    global device  
    code = []  
    data = ""  
  
 	for event in device.read_loop():  
        if event.type == evdev.ecodes.EV_KEY and event.value == 1:  
            e_code = event.code - 1  
 	        if 1 <= e_code <= 10:  
                digit = str(0)  
                if e_code != 10:  
                    digit = str(e_code)  
                code.append(digit)  
            elif e_code == 52:  
                code.append('/')  
            elif e_code == 11:  
                code.append('-')  
            elif e_code == 27:  
                data = data.join(code)  
                break  
  
 return data
```
После успешного считывания, сервис формирует json и отправляет его методом POST в главный сервис.
```python
def send_request(qr_code: str):  
    data = {'qr': qr_code}  
    answer = requests.post(QR_URL, data=json.dumps(data), headers=HEADERS)  
```
### Конфигурация
В файле конфигурации прописывается конечная точка, куда отправляется запрос и порт считывающего устройства:
```python
HEADERS = {'Content-Type': 'application/json'}  
QR_URL = 'http://127.0.0.1:80/v1/slots/qr'  
  
PORT = '/