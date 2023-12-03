"""
создайте алхимичный engine (при помощи create_async_engine)
добавьте declarative base (свяжите с engine)
создайте объект Session на основе класса AsyncSession
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from pathlib import Path
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    relationship,
)
import asyncio

BASE_DIR = Path(__file__).parent
# PG_CONN_URI = (
#     os.environ.get("SQLALCHEMY_PG_CONN_URI")
#     or "postgresql+asyncpg://postgres:password@localhost:5430/postgres"

PG_CONN_URI = "postgresql+asyncpg://postgres:password@localhost:5430/postgres"

DB_ECHO = True
async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=DB_ECHO,
)

Session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


class User(Base):
    """
    Класс User — это класс модели SQLAlchemy, который наследуется от декларативного базового класса Base,
    предоставляемого SQLAlchemy.
    Класс User представляет собой таблицу в базе данных со столбцами для
    ** имени,
    ** имени пользователя,
    ** адрес электронной почты
    ** связи с классом модели Post.
    --- Содержание класса:
    * `name`, `username` и `email` определяются как объекты `Column`.
    Каждый столбец представляет поле в таблице и имеет тип String.
    Для параметра `nullable` установлено значение `False`, что означает, что эти столбцы не могут быть `None`.
    Оба параметра `default` и `server_default` имеют пустую строку, что указывает на то, что значением
    по умолчанию для этих столбцов является пустая строка.
    * Атрибут `posts` определяется как связь с классом модели `Post` с использованием функции `relationship`,
    предоставляемой SQLAlchemy. Эта связь представляет собой связь «один ко многим»,
    где каждый «Пользователь» может иметь несколько связанных с ним объектов «Post».
    Параметр back_populates указывает атрибут в классе Post, который представляет обратную связь.
    * Метод `__repr__` определен для возврата строкового представления объекта `User`.
    Строковое представление включает имя класса и значения атрибутов `id`, `name`, `username` и `email`.
    * Метод `__str__` определен для возврата строкового представления объекта `User`.
    Строковое представление включает имя класса и значения атрибутов `id`, `name`, `username` и `email`.

    Этот класс можно использовать для определения таблицы в базе данных и взаимодействия с
    пользовательскими данными с помощью SQLAlchemy.
    """

    name = Column(String, nullable=False, default="", server_default="")
    username = Column(String, nullable=False, default="", server_default="")
    email = Column(String, nullable=False, default="", server_default="")

    posts = relationship("Post", back_populates="user", uselist=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}  "
            f"(id={self.id}, name={self.name!r}, userName={self.username!r}, email={self.email!r})"
        )


class Post(Base):
    """
    Класс Post — это класс модели SQLAlchemy, который наследуется от декларативного базового класса Base,
    ...
    * user_id представляет собой связь внешнего ключа ForeignKey со столбцом id модели User.
    * Атрибут users определяется как связь с моделью User с использованием метода relationship,
    предоставляемого SQLAlchemy. Это отношение представляет собой отношение «один к одному»,
    где каждое сообщение имеет один связанный объект User.
    Параметр back_populates указывает на атрибут в классе User,
    который представляет обратную связь (relationship)
    Для параметра uselist установлено значение False, указывающее, что это связь «один к одному».
    """

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String(255), nullable=False, default="", server_default="")

    user = relationship("User", back_populates="posts", uselist=False)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}  "
            f"(id={self.id}, userId={self.user_id}, title={self.title!r}, body={self.body!r})"
        )
