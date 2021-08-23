## 1. Подготовка
Шаг 1: подготовка главного сервиса
1. Собрать последнюю версию главного сервиса (в папке с модулем главного сервиса: `gradlew.bat installDist`)
2. Скопировать содержимое папки *project_services_path/main_service/build/install/main_service/* в папку *path_to_deploy_folder/main_service/*
3. Скопировать руководство пользователя в папку *path_to_deploy_folder/main_service/manual* (имя манула должно совпадать с настроками сервиса)

Шаг 2: подготовка клиента
1. Собрать последнюю версию киентсого приложения (в папке с проектом: `flutter build web`)
2. Скопировать содержимое папки *project_client_path/build/web/* в папку *path_to_deploy_folder/main_service/static*

Шаг 3: подготовка остальных сервисов
1. Скопировать все необходимые папки с сервисами в папку *path_to_deploy_folder/hardware_services/*
----
## 2. Отправка файлов
> Следующие действия выполняются в папке с сформированными папками.

Щаг 4: отправка данных на сервер
1. Сгенерировать архивы (в корне папки для отправки на сервер): 
    1. `tar -c -f hardware_services.tar.gz hardware_services`
    2. `tar -c -f main_service.tar.gz main_service`
    3. `tar -c -f service_configs.tar.gz service_configs`
2. Отправить файлы на сервер по SSH:
    1. `scp hardware_services.tar.gz pi@10.0.36.236:/home/pi/`
    2. `scp main_service.tar.gz pi@10.0.36.236:/home/pi/`
    3. `scp service_configs.tar.gz pi@10.0.36.236:/home/pi/`
3. Распаковать архивы:
    1. `tar -xvf hardware_services.tar.gz`
    2. `tar -xvf main_service.tar.gz`
    3. `tar -xvf service_configs.tar.gz`
---
## 3. Подготовка окружения 
> Данный пункт можно пропустить если виртуальное окружение уже было настроено

Шаг 5: настройка окружения (операции выполняются на сервере (подкоючиться можно по ssh) в корне папке пользователя)
1. Установите gunicorn: 
    * `pip3 install gunicorn`
2. Включение поддержки управлением пинами малины:
    2. `sudo apt install python3-rpi.gpio`
3. Установка Flask 
    * `pip3 install Flask`
4. Остальные библиотеки:
    1. `pip3 install requests`
    2. `pip3 install serial`
    3. `pip3 install SMBus`
    4. `pip3 install evdev`
---
## 4. Запуск
> ### Важно 
> Перед следующими действиями проверьте, что вы сохранили все данные баз данных, истории операций и логов системы, чтобы избежать возможной потери данных.

Шаг 6: распаковываем архивы
* `tar -xvf hardware_services.tar.gz`
* `tar -xvf main_service.tar.gz`
* `tar -xvf service_configs.tar.gz`

Если до этого уже были данные, то после разархтивации, данные должны замениться, важно проверить, что данные необходимые данные не перетерлись. Если прошлые данные лежат в других папках, необходимо скопировать их в новые папки. 

Шаг 7: запуск сервисов
1. Копируем файлы конфигурации в загрузку *systemd*
    * `sudo cp -R service_configs/* /etc/systemd/system/`
2. Перезагружаем *systemd*
    * `sudo systemctl daemon-reload`
3. Запускаем сервисы. Для каждого сервиса выполнить:
    * `sudo systemctl start *service_name*`
    
    Имя сервиса совпадает с именем файла конфигурации. Например, 
    * `sudo systemctl start workshop_system_button` 

    Запускает сервис *workshop_system_button*
4. Добавляем сервисы в автозагрузку. Аналогично прошлому шагу для каждого сервиса выполняем команду:
    * `sudo systemd enbale *service_name*`

## Готово!