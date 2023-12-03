"""
Доработайте модуль jsonplaceholder_requests:
установите значения в константы USERS_DATA_URL и POSTS_DATA_URL (ресурсы нужно взять отсюда https://jsonplaceholder.typicode.com/)
создайте асинхронные функции для выполнения запросов к данным ресурсам (используйте aiohttp)
рекомендуется добавить базовые функции для запросов, которые будут переиспользованы (например fetch_json)
"""
import aiohttp

# import asyncio

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def common_fetch_json(url: str, column_names: list) -> list:
    """
    :param column_names: Закидываем список ключей в качестве параметра
    :param url: Закидываем URL в качестве параметра
    :return: Возвращаем результат -> список словарей с заданными ключами
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result: list = await response.json()
            filtered_result: list = []
            for item in result:
                # print(item)
                filtered_user_data: dict = {
                    key: value
                    for key, value in item.items()
                    if key in column_names
                }
                filtered_result.append(filtered_user_data)
            # print(filtered_result)
            return filtered_result


async def get_users_list_from_url(
    service: str = USERS_DATA_URL,
) -> list:
    column_names: list = ["name", "username", "email"]
    users_data: list = await common_fetch_json(service, column_names)
    return users_data


async def get_posts_list_from_url(
    service: str = POSTS_DATA_URL,
) -> list:
    column_names: list = ["userId", "title", "body"]
    posts_data: list = await common_fetch_json(service, column_names)
    return posts_data


# async def main():
#     # result = await common_fetch_json(USERS_DATA_URL)
#     result_users = await get_users_dict_from_url()
#     result_posts = await get_posts_dict_from_url()
#     print(result_users)
#     print()
#     print(result_posts)
#
#     pass
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
