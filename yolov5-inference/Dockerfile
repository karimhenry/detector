# syntax=docker/dockerfile:1
FROM python:3.10-slim
RUN  apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]