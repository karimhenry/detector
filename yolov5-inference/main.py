import time
import os
import redis
from flask import Flask
import subprocess
import datetime


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def infer():
    # Get the current date and time
    now = datetime.datetime.now()
    # Convert the date and time to an integer using the timestamp() method
    timestamp = str(int(now.timestamp()))

    # Print the integer value
    # print(timestamp)

    # frame = 
    os.system(f"ffmpeg -i rtsp://rtsp-server1:8554/test.sdp -vframes 1 data/images/output_file{timestamp}.jpg -y")
    t1= os.system(f"python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images/output_file{timestamp}.jpg --exist-ok")
    # return str(t1)
    output_path = f"C:/Users/Karim Henry/Desktop/tahaluf/yolo_detector/yolov5-inference/runs/detect/exp/output_file{timestamp}.jpg"
    cache.set('path', output_path)
# True
    # cache.get('foo')
    return cache.get('path')


@app.route('/loc')
def identify():
    return cache.get('path')

    # return "c://users/.."

# @app.route('/loc1')
# def images(image):
#     return "c://users/.."
    # t1= os.system("python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images/bus.jpg")
    # return str(t1)

# def hello():
#     # count = get_hit_count()
#     message ="hello"
#     result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
#     # print(result)
#     with open('output.txt',"w") as f:
#         f.write(str(count))
#     # return 'Hello KIMO World! I have been seen {} times.\n'.format(count)
#     return result.stdout