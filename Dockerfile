FROM python:3.11-alpine

WORKDIR /bot

RUN pip install pipenv
RUN pip install --upgrade pip setuptools

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .