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
        # print(imgdata[0:200])
        # imgdata = imgdata[:-3]
        # print(imgdata[0:200])
        # print(type(imgdata))
        
        imgdata = imgdata[15:]
        filename = "./test/imageToSave.jpeg"  
        with open(filename, 'wb') as f:
            f.write(imgdata)            
        # with open("./test/imageToSave.jpeg", "wb") as fh:
        #     fh.write(base64.decodebytes(img_data.encode()))
        # img_data_bytes = base64.decodebytes(img_data.encode())
        # im_bytes = base64.b64decode(img_data_bytes)   # im_bytes is a binary image
        # im_file = BytesIO(im_bytes)  # convert image to file-like object
        # img = Image.open(im_file) 
        # img.save("./test/imageToSave.jpeg")
        time.sleep(0.2)
        
        p1 = subprocess.Popen(['python', "transform_image.py"])

        p1.wait()

    return {"status":"good"}

if __name__ == '__main__':
    app.run()
