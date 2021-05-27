#! /bin/bash
python3 -m venv env
source "./env/bin/activate"
python3 -m pip install -r requirements.txt
# setup directory structures
mkdir images
mkdir images/images_2d
mkdir images/images_3d
mkdir images/images_effected
python main.py
# works for sure untill here
# cd frontend
# python3 -m http.server
# open http://localhost:8000/

