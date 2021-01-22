FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt
COPY ./api /api

RUN pip install -r /requirements.txt

WORKDIR /api

USER root