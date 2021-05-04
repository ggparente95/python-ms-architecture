# pull official base image
FROM python:3.10.0a7-alpine3.13

# set work directory
WORKDIR /usr/src/ms-flask

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apk add build-base

COPY ./requirements.txt /usr/src/ms-flask/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/ms-flask/
