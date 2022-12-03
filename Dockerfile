FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]

