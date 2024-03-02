import os
import redis
from flask import Flask, make_response, render_template, send_file
import datetime


app = Flask(__name__,template_folder='templates')
cache = redis.Redis(host='redis', port=6379)
persistant = os.environ['PERSISTANT']

@app.route('/', methods=["GET"] )
def infer():
    now = datetime.datetime.now()
    timestamp = str(int(now.timestamp()))
    t1=0
    t2=0
    t1 = os.system(f"ffmpeg -i rtsp://rtsp-server1:8554/test.sdp -vframes 1 data/images/output_file{timestamp}.jpg -y")
    t2 = os.system(f"python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images/output_file{timestamp}.jpg --exist-ok")
    if t1 ==0 & t2==0:
        persistant = os.environ['PERSISTANT']
        output_path = f"{persistant}/yolo_detector/yolov5-inference/runs/detect/exp/output_file{timestamp}.jpg"
        cache.set('path', output_path)
        response = make_response(f"<h1>Output Path: </h1><h3>{output_path}</h3>", 200)
        output_path = output_path.split("yolov5-inference/")[-1]
        return send_file(output_path)
        # # return render_template("index.html", image_path=output_path)
        # return render_template("index.html", path=output_path)
    else:
        response = make_response("<h1>Internal Server Error</h1>", 500)
        return response

@app.route('/loc')
def identify():
    return cache.get('path')
