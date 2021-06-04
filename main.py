import flask
from flask_cors import CORS, cross_origin
from PIL import Image
import base64
from io import BytesIO
# import transform_image
import subprocess
import time


app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.debug = True
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/give_image', methods=["POST", "GET"])
@cross_origin()
def respond():
    data = flask.request.get_json()
    # print(data)

    if data is None:
        print("No valid request body, json missing!")
        return flask.jsonify({'error': 'No valid request body, json missing!'})
    else:
        img_data = data['image']
        # print(type(img_data))
        img_data += '=' * (-len(img_data) % 4)
        imgdata = base64.decodebytes(img_data.encode())

        imgdata = imgdata[15:]
        #todo gotta change this
        filename = "./images/imageToSave.jpeg"  
        with open(filename, 'wb') as f:
            f.write(imgdata)            

        time.sleep(0.2)
        
        p1 = subprocess.Popen(['python', "transform_image.py"])

        p1.wait()

        file_vid = flask.send_file("./imageToSave.mp4")

    return file_vid

if __name__ == '__main__':
    app.run()
