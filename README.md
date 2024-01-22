# BotAds API
Интеграция сервиса по автоматической покупке/продаже Telegram трафика - <a href="https://t.me/Bot_Ads_Bot">``BotAds``</a>



## Установка

```bash
pip install git+https://github.com/BotAdsCod/botads.git
```

## Зависимости

 - ``Python 3.7+``
 - ``aiohttp``

## Как это работает?
Перед выполнением определенных действий ваш бот отправляет запрос на проверку подписок с помощью метода ``subs_check``. Результатом будет отправка пользователю сообщения со списком спонсоров, если они есть, и метод вернет значение ``True``. В случае, если пользователь уже выполнил все спонсорские задания, метод вернет значение ``False``, что означает, что для пользователя нет действующих заданий или он уже выполнил все.


## Пример использования с фреймворком aiogram 3

```python
from botadsapi import BotAds

from aiogram import types

router = Router(name="example_router")
dp.include_router(router)

botads = BotAds(API_KEY)

#Ваша функция
@router.message(F.text=='Привет') 
async def message_handler(message: types.Message):
    if not await botads.subs_check(message.from_user.id):
        return
    #Ваш код который выполняется если для пользователя нет спонсорских заданий

#Вызывается при нажатии кнопки проверки подписки
@router.callback_query(F.data=='check') 
async def check(call: types.CallbackQuery):
    if not await botads.subs_check(call.from_user.id):
        await call.answer("❌ Подпишитесь на все каналы!", show_alert=True)
    else:
        #Ваш код, который выполняется после прохождения всех спонсорских заданий
```

Если у вас возникли вопросы по подключению, обращайтесь по контактам, указанным в описании <a href="https://t.me/Bot_Ads_Bot">``BotAds``</a>
