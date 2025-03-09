# Diplom_2

# Автотесты API для сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site)

Сервис [Stellar Burgers](https://stellarburgers.nomoreparties.site) - это сайт для заказа бургеров.

Его документация: [API](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89/).


## Структура проекта 

* [tests](tests) - директория с тестами
* [tests](tests/create_order_test.py) - файл с проверками списка заказов юзера
* [tests](tests/get_user_orders_test.py) - файл с проверками совершения заказа
* [test](tests/sign_in_user_test.py) - файл с проверками логина юзера
* [test](tests/sign_up_user_test.py) - файл с проверками регистрации юзера
* [test](tests/update_user_data_test.py) - файо с проверками обновления данных юзера
* [data.py](data.py) - файл с данными юзера
* [urls.py](urls.py) - файл с эндроинтами
* [allure_results](allure_results) - каталог с отчетом тестирования
* [conftest.py](tests/conftest.py) - файл с фикстурами
* [helpers.py](helpers.py) - файл с вспомогательными методами и классами

## Запуск автотестов

**Установка зависимостей**
```bash
pip install -r requirements.txt
```

Для запуска тестов выполнить:
```bash
pytest tests --alluredir=allure_results
```

Для генерации репорта выполнить:
```bash
allure generate --single-file allure_results -o allure_report
```