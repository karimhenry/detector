FROM python:3
RUN apt update
RUN apt upgrade -y
RUN apt install vlc -y
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN sed -i 's/geteuid/getppid/' /usr/bin/vlc
WORKDIR /code
COPY . .
ARG MP4_FILENAME
CMD cvlc -vvv videos/$MP4_FILENAME --sout '#rtp{sdp=rtsp://0.0.0.0:8554/test.sdp}' --sout-keep --no-sout-all --loop
