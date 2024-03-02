# RTSP-to-Inference Pipeline with Docker Compose
This project implements a solution that utilizes Docker containers to process video streams, and uses YOLOv5 model to perform object detection for a frame captured from rtsp stream.

# Components:

- RTSP container (Camera): Simulates a surveillance camera by streaming a video as an RTSP feed on repeat.
- Inference Flask container: Analyzes the RTSP stream using a YOLOv5 model.
- Redis container: Captures the path for last frame captured from stream.
- Python script: Triggers inference on the Flask container and retrieves results.
# Functionalities:

1. The RTSP container continuously streams a video through the command run in `rtsp-server/Dockerfile`
2. The Inference Flask container `yolov5-inference/main.py` applies this logic:
    - Receives requests.
    - Loads a YOLOv5 model.
    - Captures a frame from the RTSP stream.
    - Performs object detection using the YOLOv5 model.
    - Draws bounding boxes around detected objects on the frame.
    - Saves the processed image to an external directory.
    - Returns the path to the saved image in the response.
    - Captures the path for last frame streamed and caches it into redis db.
3. The Python script `request.py` sends a request to the Inference Flask container and prints the path to the output image.
# Implementation:

Docker Compose is used to manage and orchestrate the containers.
The RTSP container serves as a dependency for the Inference Flask container.
# Benefits:

Modular and scalable architecture.
Containerized environment simplifies deployment and management.
Easy integration with other applications.
# Getting Started:

- Clone this repository.
- Put the video of interest inside the `rtsp-server/videos` and set `MP4_FILENAME` environment variable to be the same name as video of interest.   
- Set the `PERSISTANT` environment variable in the `docker-compose.yml` file to the location where you clone this repo.
- Build and start the containers using `docker-compose up`.
Run the provided Python script to trigger inference and see the output image path.
- To send request, go to browser and hit this url: `https:localhost:8000`
- To identify persistant location, hit this url: `https:localhost:8000/loc`
- Run `request.py` using `python request.py`. This sends request to running service to identify location of last frame captured. 
- Head to `http://127.0.0.1:5000/` on local machine with persistant directory, you will be directed to last frame captured. (containers must be running) 