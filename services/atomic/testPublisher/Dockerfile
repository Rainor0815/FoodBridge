FROM python:3.9

WORKDIR /app

COPY . /app/

RUN pip install pika

CMD ["python3", "testPublisher.py"]
