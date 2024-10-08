![banner](https://i.postimg.cc/GtfcGKzn/image-2024-04-14-22-05-40.png "banner")


<div align="center">
<h1>Интеграция сервиса онлайн оплаты CLICK SHOP API и Merchant API через фреймворк Django в Python</h1>
</div>

## Необходимые пакеты
[Django](https://docs.djangoproject.com/) - свободный фреймворк для веб-приложений на языке Python, использующий шаблон проектирования MVC.

[Django REST framework](https://www.django-rest-framework.org/) - это мощный и гибкий инструментарий для создания веб-приложений.

[Requests](https://requests.readthedocs.io/) - это элегантная и простая HTTP-библиотека для Python, созданная для людей.

## Установка
Клонируйте проект с github
```console
git clone https://github.com/JahongirHakimjonov/ClickUzIntegration.git
```

Поместите это в `settings.py`
```console
INSTALLED_APPS = [
    ...
    'rest_framework',
]

CLICK_SETTINGS = {
    'service_id': "<Ваш сервис ID>",
    'merchant_id': "<Ваш merchant ID>",
    'secret_key': "<Ваш секретный ключ>",
    'merchant_user_id': "<Ваш merchant user ID>",
}
```
> _**Примечание:**_
> Эти информации будет предоставлена ​​вам после того, как вы подписали контракт с OOO «Click»


Выполните команды `makemigrations` и `migrate`
```console
python manage.py makemigrations
python manage.py migrate
```

## Настройка биллинг
Введите `Prepare URL (Адрес проверки)` и `Complete URL (Адрес результата)` на сайт merchant.click.uz, чтобы система CLICK проверил ваш заказ.

Prepare URL
```
https://example.com/pyclick/process/click/transaction/?format=json
```
Complete URL
```
https://example.com/pyclick/process/click/transaction/?format=json
```
<br>
<img src="https://i.postimg.cc/KYymdYsH/merchant-click.png" width="70%">
<br>
<br>
<img src="https://i.postimg.cc/Vk5cpCRg/merchant-click-2.png" width="70%">

## Создать заказ

Вы можете создать заказ через [администратора django](http://127.0.0.1:8000/admin/) или по этой ссылке http://127.0.0.1:8000/pyclick/process/click/transaction/create/
<br>
<img src="https://i.postimg.cc/pXkY69Gs/django-admin-click-transaction.png" width="70%">
<br>
<br>
<img src="https://i.postimg.cc/02zbPLWp/create-click-transaction.png" width="70%">


Поместите желаемую сумму в поле `amount` и создайте заказ.

## CLICK SHOP API

Обратите внимание, что после создания заказа по этой ссылке http://127.0.0.1:8000/pyclick/process/click/transaction/create/ мы перейдем на сайт http://my.click.uz. 
<br>
<br>
<img src="https://i.ibb.co/1XYKhzB/my-click.png" width="70%">

Вы можете оплатить, введя номер карты или номер телефона. 

Полная информация, локальное тестирование, реальная интеграция с системой `CLICK SHOP API`, настройка личного кабинета и для проверки заказа через систему [Merchant CLICK](https://merchant.click.uz/) вы можете найти по этой ссылке https://pypi.org/project/python-click/0.1/



## CLICK Merchant API

### Создать инвойс (счет-фактуру)
```
POST http://127.0.0.1:8000/pyclick/process/click/service/create_invoice
```
> Body:
> ```
> phone_number - Номер телефона
> ```
> ```
> transaction_id - ID заказа
> ```
---
### Проверка статуса инвойса (счет-фактуры)
```
POST http://127.0.0.1:8000/pyclick/process/click/service/check_invoice
```
> Body:
> ```
> invoice_id - ID инвойса
> ```
> ```
> transaction_id - ID заказа
> ```
---
### Создание токена карты
```
POST http://127.0.0.1:8000/pyclick/process/click/service/create_card_token
```
> Body:
> ```
> card_number - Номер карты
> ```
> ```
> expire_date - Срок карты
> ```
> ```
> temporary - создать токен для единичного использования. Временные токены автоматически удаляются после оплаты.
> ```
> ```
> transaction_id - ID заказа
> ```
---
### Подтверждение токена карты
```
POST http://127.0.0.1:8000/pyclick/process/click/service/verify_card_token
```
> Body:
> ```
> card_token - Токен карты
> ```
> ```
> sms_code - Полученный смс код
> ```
> ```
> transaction_id - ID заказа
> ```
---
### Оплата с помощью токена
```
POST http://127.0.0.1:8000/pyclick/process/click/service/payment_with_token
```
> Body:
> ```
> card_token - Токен карты
> ```
> ```
> transaction_id - ID заказа
> ```
---
### Удаление токена карты
```
POST http://127.0.0.1:8000/pyclick/process/click/service/delete_card_token
```
> Body:
> ```
> card_token - Токен карты
> ```
---
### Снятие платежа (отмена)
```
POST http://127.0.0.1:8000/pyclick/process/click/service/cancel_payment
```
> Body:
> ```
> transaction_id - ID заказа
> ```
---
### Проверка статуса платежа
```
POST http://127.0.0.1:8000/pyclick/process/click/service/check_payment_status
```
> Body:
> ```
> transaction_id - ID заказа
> ```
---

Вы можете отправить эти запросы через [Postman](https://www.postman.com/). Загрузите [эту коллекцию](https://drive.google.com/file/d/1G1xTfVIzQBf8ebqcjEzn_w9m6sXeiXBp/view) и импортируйте ее в свой `postman`. В этой коллекции все запросы и обязательные поля написано.

Для более подробной информации, создание заказа, `production` интеграция с системой `CLICK SHOP API` и `Merchant API`, настройка личного кабинета и для проверки заказа через систему [Merchant CLICK](https://merchant.click.uz/)


## Спасибо за внимание!

## Автор
[Jahongir Hakimjonov](https://t.me/ja_khan_gir)

## Социальные сети
<div align="center">
  Подпишитесь на нас, чтобы получать больше новостей о веб-программировании: <br>
  <a href="https://www.instagram.com/ja_khan_gir">Instagram</a>
  <span> | </span>
  <a href="https://t.me/ja_khan_gir">Telegram</a>
</div>
# ClickUzIntegration
