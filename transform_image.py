# import subprocess
import uuid
import moviefy
import makestl
import add_effects
import uuid
import os
import shutil



def transform_image(image_path,double=False,frames=10, cleanup=True):
    # print("hello world")
    unique_id = uuid.uuid4()
    img_file = image_path
    new_file = "./images/images_3d/"+ str(unique_id) +".stl"
    makestl.make_stl(img_file, new_file)
    add_effects.create_movie(img_file,new_file,unique_id=unique_id,frames=frames)
    moviefy.moviefy(unique_id,"image")
    if cleanup:
        os.remove(new_file)
        shutil.rmtree('./images/images_effected/'+ str(unique_id))

image_path = "./images/images_2d/cool_lion.jpeg"
transform_image(image_path,frames=10)