# import subprocess
import uuid
import moviefy
import makestl
import add_effects
import uuid
import os
import shutil
import time




def transform_image(image_path,double=False,frames=10, cleanup=True, make_mov=True):
    # print("hello world")
    unique_id = uuid.uuid4()
    img_file = image_path
    just_name = os.path.basename(img_file).split(".")[0]
    
    new_file = "./images/images_3d/"+ str(unique_id) +".stl"
    makestl.make_stl(img_file, new_file)
    time.sleep(0.1) #helps make sure program does not bug out 
    add_effects.create_movie(img_file,new_file,unique_id=unique_id,frames=frames)
    time.sleep(0.1)
    if make_mov:
        moviefy.moviefy(unique_id,just_name,frames)
    if cleanup:
        os.remove(new_file)
        shutil.rmtree('./images/images_effected/'+ str(unique_id))


# TESTS
image_path = "./images/images_2d/cool_lion.jpeg"
transform_image(image_path,frames=1,cleanup=True)

image_path = "./images/images_2d/snake.jpeg"
transform_image(image_path,frames=1,cleanup=True,make_mov=True)

image_path = "./images/images_2d/nora.jpeg"
transform_image(image_path,frames=1,cleanup=True,make_mov=True)