## образ: docker build ./homework_03 -t app
## запуск docker контейнера: docker run -p 8000:8000 -it app

FROM python:3.11.4-bookworm
LABEL authors="Aleksandr"

EXPOSE 8000

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]




