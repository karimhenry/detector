import requests
import os
from flask import Flask, make_response, render_template,send_file

app = Flask(__name__,template_folder='.')

@app.route('/', methods=["GET"] )
def infer():
    container_url = "http://localhost:8000"  
    try:
        response = requests.get(container_url + "/loc")
        print("Request successful:", response.text)
        output_path = response.text   
        output_path = output_path.split("yolo_detector/")[-1]
        print(output_path)
        return send_file(output_path)
    except:
        return make_response("<h1>URL Not Found</h1>", 404)

if __name__=="__main__":
    app.run(debug=True)

# # Replace with the container's alias in the network
# container_url = "http://localhost:8000"  # Replace with actual alias and port

# # Example request (adjust based on your API endpoint)
# response = requests.get(container_url + "/loc")
# print(response)
# # Check response status code
# if response.status_code == 200:
#     print("Request successful:", response.text)
# else:
#     print("Error:", response.status_code, response.text)