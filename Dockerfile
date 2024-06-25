FROM python:alpine3.20
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

