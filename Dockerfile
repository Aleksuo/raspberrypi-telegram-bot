FROM python:3-alpine as base

WORKDIR /app

COPY . .
RUN apk add --no-cache build-base\
    libffi-dev\
    libressl-dev &&\
    pip install -r requirements.txt

CMD ["python", "./src/start.py"]