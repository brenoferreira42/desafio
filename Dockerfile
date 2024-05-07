FROM python:latest as desafio

WORKDIR /app

COPY . /app/

CMD ["python", "main.py"]
