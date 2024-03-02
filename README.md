# RTSP-to-Inference Pipeline with Docker Compose
This project implements a high-level design for a solution that utilizes Docker containers to process video streams.

# Components:

- RTSP container (Camera): Simulates a surveillance camera by streaming a video as an RTSP feed on repeat.
- Inference Flask container: Analyzes the RTSP stream using a YOLOv5 model.
- Python script: Triggers inference on the Flask container and retrieves results.
# Functionalities:

1. The RTSP container continuously streams a video.
2. The Inference Flask container:
    - Receives requests.
    - Loads a YOLOv5 model.
    - Captures a frame from the RTSP stream.
    - Performs object detection using the YOLOv5 model.
    - Draws bounding boxes around detected objects on the frame.
    - Saves the processed image to an external directory.
    - Returns the path to the saved image in the response.
3. The Python script sends a request to the Inference Flask container and prints the path to the output image.
# Implementation:

Docker Compose is used to manage and orchestrate the containers.
The RTSP container serves as a dependency for the Inference Flask container.
# Benefits:

Modular and scalable architecture.
Containerized environment simplifies deployment and management.
Easy integration with other applications.
# Getting Started:

- Clone this repository.
- Build and start the containers using `docker-compose up`.
Run the provided Python script to trigger inference and see the output image path.
- To send request, go to browser and hit this url: `https:localhost:8000`


