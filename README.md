# MobileDogs_API #
Выполнили: Конова и Галиулина

## Описание проекта ##
Создать приложение, в котором пользователи могут выбрать бездомных собак, за которыми они будут следить. При добавлении собаки пользователю будут отправляться данные о её передвижении и состоянии. Также пользователи смогут давать задания, касающиеся помощи собакам, другим пользователям, если по какой-то причине он сам не имеет возможности помочь

## Роль устройств(ошейников): ##
1. Отслеживания местоположения собак
2. Отслеживания их состояния здоровья по движению(если долго не движется, то что-то не так)

## Сценарии: ##
1. Авторизация пользователей: пользователь отправляет на сервер свой номер телефона и пароль -> если в базе данных есть его номер телефона и пароль совпадает, то пользователь входит в аккаунт
2. Регистрация пользователей: пользователь отправляет на свервер свой номер телефона и пароль -> в базе создаётся новая запись с его уникальным id, номером телефона и паролем
3. Регистрация ошейников: при активации ошейника на сервер отправляются код ошейника, фото собаки, кличка собаки -> создаётся запись в базе данных с кодом ошейника, кличкой собаки и фото собаки
4. Привязка ошейников﻿ и пользователей: пользователь смотрит фото собак поблизости и выбирает какую добавить -> пользователь отправляет на сервер запрос с id ошейника выбранной собаки и из его профиля берётся его id -> в базе данных для связи пользователей и собак создаётся новая запись с полями id пользователя и id ошейника
5. Оповощение пользователей: берется id ошейника и проверяется у каких пользователей есть этот id в таблице -> пользователям, привязанным к собаке отправляется данные с ошейника этой собаки, если, допустим, она давно не двигалась 
6. Модерирование: если у пользователя низкий уровень заряда на телефоне, или состояние ошейника плохое, или подвижность собаки нулевая уже долгое время, то ему приходит уведомление
7. Задание от одних пользователям другим, верификацию выполнения заданий: берется id пользователя, который отправил запрос на отправку заданий, текст задания и id собаки, задание добавляется в бд, далее берутся id пользователей, которые находятся близко к собаке и им приходит уведомление об этом задании с его текстом, пользователи нажимают на принять и отклонить, и статус задания меняется на "в процессе", после выполнения задания пользователь нажимает на кнопку готово с фотоотчетом и комментарием и статус меняется на готово
8. Если собака не двигается: собака долго не двигаетсся -> ошейник подаёт сигнал пользователям, к которым добавлена эта собака или админу, если устройство ни на кого не зарегистрировано -> пользователь идёт к собаке и проверяет жива ли она, или даёт это заание другим пользователям

## Необходимые запросы, чтобы реализовать сценарии выше: ##
### 1. Регистрация пользователя:
Что вводит пользователь:
```
  {
  login: str - логин пользователя
  password: str - пароль пользователя
  }
```
Если логин пользователя не занят, то пользователю будет выдан токен:
```
  {
  success: bool
  accessToken: str
  }
```
Если такой пользователь уже существует, то будет вызвано исклюение _**BusyLogin**_

### 2. Авторизация:
Что вводит пользователь:
```
  {
  login: str - логин пользователя
  password: str - пароль пользователя
  accessToken: str - токен пользователя
  }
```
Если всё введено правильно, то пользоватулю выдаётся сообщение о том, что он успешно вошёл в аккаунт:
```
  {
  success: bool 
  message: str
  }
```
Если в базе данных нет польователя с таким логином, то будет вызвано исключение _**WrongLogin**_

Если введённый пароль не совпадает с паролем выбранного пользователя, то будет вызвано исключение _**WrongPassword**_

Если введённый токен не совпадает с токеном выбранного пользователя, то будет вызвано исключение _**WrongToken**_

### 3. Регистрация собаки:
Что вводит пользователь:
```
  {
  name: str - кличка собаки
  collar_id: str - id регистрируемого ошейника
  }
```
Если ошейник с таким id не занят, то будет выдан токен ошейника:
```
  {
  success: bool
  accessToken: str
  }
```
Если ошейник с таким id уже занят, то будет вызвано исклюение _**BusyCollar**_

### 4. Создание подписки на собаку:
```
   {
   "user_login": "string" - логин пользователя
   "collar_id": "string" - id ошейника собаки, на которую пользователь подписывается
   "accessToken": "string" - токен пользователя
   }
```
Если пользователь еще не подписан на эту собаку, то пользователю будет возвращен его токен:
```
   {
   "success": true,
   "accessToken": "string" 
   }
```
### 5. Отписка от собаки:
Что вводит пользователь:
```
   {
   "user_login": "string" - логин пользователя
   "collar_id": "string" - id ошейника собаки, от которой пользователь отписывается
   "accessToken": "string" - токен пользователя
   }
```
Если пользователь подписан на эту собаку, то ему будет возвращено сообщение:
```
   {
   "success": true,
   "accessToken": "string" 
   }
```
4. Привязка ошейников и пользователей:
```
  {
      логин пользователя,
      id ошейника,
      токен
  }
```
5. Оповощение пользователей:
```
   {
      id ошейника,
      состояние ошейника/собаки
   }
```
6.  Модерирование:
```
  {
      id ошейника,
      состояние ошейника/собаки
   }
```
### Установка и использование: ###

1. Необходимо склонировать репозиторий
2. Перейдите в папку MobileDogs_API
3. Напишите команду в консоли python main.py
4. Перейдите по выданному адресу и делайте запросы
   
