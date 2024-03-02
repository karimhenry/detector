FROM python:3
RUN apt update
RUN apt upgrade -y
RUN apt install vlc -y
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN sed -i 's/geteuid/getppid/' /usr/bin/vlc
WORKDIR /code
COPY . .
CMD cvlc -vvv videos/people.mp4 --sout '#rtp{sdp=rtsp://0.0.0.0:8554/test.sdp}' --sout-keep --no-sout-all --loop
