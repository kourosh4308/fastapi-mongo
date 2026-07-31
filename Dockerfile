FROM python:3.14
WORKDIR /home/app
COPY . .
RUN pip install fastapi uvicorn pymongo