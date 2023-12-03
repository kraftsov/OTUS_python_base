"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from models import async_engine, Session, Base, User, Post
from jsonplaceholder_requests import (
    get_users_list_from_url,
    get_posts_list_from_url,
)


# Создание таблиц
async def init_models():
    async with async_engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()


# Loading Users
async def add_users_in_table(
    users_data: list,
):
    async with Session() as session:
        async with session.begin():
            for any_user in users_data:
                user_added = User(
                    name=any_user["name"],
                    username=any_user["username"],
                    email=any_user["email"],
                )
                session.add(user_added)


# Loading Posts
async def add_posts_in_table(
    posts_data: list,
):
    async with Session() as session:
        async with session.begin():
            for any_post in posts_data:
                post_added = Post(
                    user_id=any_post["userId"],
                    title=any_post["title"],
                    body=any_post["body"],
                )
                session.add(post_added)


# Main function -------------------------------------------------------------
async def async_main():
    await init_models()
    user_data, post_data = await asyncio.gather(
        get_users_list_from_url(),
        get_posts_list_from_url(),
    )
    print("------------ПОЛЬЗОВАТЕЛИ-------------:")
    enumerate(user_data)
    for item in enumerate(user_data):
        print(item)

    print("---------------ПОСТЫ-----------------:")
    enumerate(post_data)
    for item in enumerate(post_data):
        print(item)
    print("--------------------------------------end")
    await add_users_in_table(user_data)
    await add_posts_in_table(post_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
