# syntax=docker/dockerfile:1
# FROM yolov5:v1
# RUN  apt-get update 
# RUN apt-get install ffmpeg libsm6 libxext6  -y
# WORKDIR /code
# ENV FLASK_APP=main.py
# ENV FLASK_RUN_HOST=0.0.0.0
# # RUN apk add --no-cache gcc musl-dev linux-headers
# # RUN  apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# # sudo 
# EXPOSE 5000
# # WORKDIR /code/yolov5_inference
# CMD ["flask", "run"]
FROM python:3.10-slim
RUN  apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y

# FROM yolov5:v1
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# CMD ["python","main.py"]
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]