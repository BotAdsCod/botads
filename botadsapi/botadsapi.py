from typing import Any

import aiohttp

class BotAds:

    def __init__(self, api_key: str, count_places: int = 8):
        self.api_key = api_key
        self.count_places = count_places
        self._timeout = 5

    def __preset_args(self, user_id: int, count_places: int, first_name: str = "", language_code: str = ""):
        if count_places == -1:
            count_places = self.count_places

        headers = {'Content-Type': 'application/json'}
        json = {'api_key': self.api_key, 'user_id': user_id, 'count_places': count_places}
        if first_name != "" or language_code != "":
            json = {**json, **{'first_name': first_name, 'language_code': language_code}}

        return {'headers': headers, 'json': json, 'timeout': self._timeout}

    @staticmethod
    async def __api_post(url, args):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, **args) as response:
                if response.ok:
                    return await response.json()
        return False

    async def subs_check(self, user_id: int, first_name: str = "", language_code: str = "ru",
                         count_places: int = -1) -> bool:
        """
        Используйте этот метод для проверки наличия доступных спонсорских заданий для вашего бота.

        Source: https://api.botads.pro/docs#/default/subs_check_bot_subs_check_post

        :param language_code: Необходимо передавать язык клиента
        :param first_name: Необходимо передавать Имя пользователя
        :param user_id: Идентификатор пользователя, которому необходимо отправить сообщение.
        :param count_places: Максимальное количество мест
        :return: Возвращает значение True, если список заданий пуст или если пользователь выполнил все задания.
        """
        if not self.api_key:
            return True

        args = self.__preset_args(user_id, count_places, first_name, language_code)
        if res_req := await self.__api_post('http://api.botads.pro:5000/bot/subs_check', args):
            return res_req.get('checked')
        return True

    async def get_subs_list(self, user_id: int, first_name: str = "", language_code: str = "ru",
                            count_places: int = -1) -> list[Any] | Any:
        """
        Используйте этот метод, чтобы получить список спонсорских заданий и самостоятельно отправлять сообщение пользователям.

        Source: https://api.botads.pro/docs#/default/get_subs_list_bot_get_subs_list_post

        :param language_code: Необходимо передавать язык клиента
        :param first_name: Необходимо передавать Имя пользователя
        :param user_id: Идентификатор пользователя, которому необходимо отправить сообщение.
        :param count_places: Максимальное количество мест на ОП, если значение не указано, будет установлено по умолчанию при инициализации экземпляра класса BotAds.
        :return: Возвращает список спонсорских заданий в формате [{"id": 123456, "link": "https://t.me/examplelink", "title": "Заголовок канала"}]
        """
        if not self.api_key:
            return []

        args = self.__preset_args(user_id, count_places, first_name, language_code)
        if res_req := await self.__api_post('http://api.botads.pro:5000/bot/get_subs_list', args):
            return res_req.get('unfollow_subs')
        return []
