FROM arm32v7/python:3-alpine

WORKDIR /app

COPY . .
RUN apk add --no-cache build-base\
    libffi-dev\
    libressl-dev &&\
    sudo pip install -r requirements.txt 

ENTRYPOINT ["python", "/app/src/run.py"]