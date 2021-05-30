# import subprocess
import uuid
import moviefy
import makestl
import add_effects
import uuid
import os
import shutil
import time
from  PIL import Image


def transform_image(image_path,double=False,frames=10, cleanup=True, make_mov=True):
    # print("hello world")
    unique_id = uuid.uuid4()
    img_file = image_path
    just_name = os.path.basename(img_file).split(".")[0]
    image = Image.open("./images/imageToSave.jpeg")
    new_image = image.resize((800, 800))
    image.close()
    new_image.save("./images/imageToSave.jpeg")
    new_image.close()
    new_file = "./images/images_3d/"+ str(unique_id) + ".stl"
    makestl.make_stl(img_file, new_file)
    time.sleep(0.1) #helps make sure program does not bug out 
    if double:
        add_effects.create_movie3(img_file,new_file,unique_id=unique_id,frames=frames)
    else:
        add_effects.create_movie2(img_file,new_file,unique_id=unique_id,frames=frames)
    time.sleep(0.1)
    if make_mov:
        moviefy.moviefy(unique_id,just_name,frames)
    if cleanup:
        os.remove(new_file)
        shutil.rmtree('./images/images_effected/'+ str(unique_id))


# TESTS
if __name__ == "__main__":
    # try:
    #     image_path = "./images/images_2d/cool_lion.jpeg"
    #     transform_image(image_path,frames=1,cleanup=True)

    #     image_path = "./images/images_2d/snake.jpeg"
    #     transform_image(image_path,frames=1,cleanup=True,make_mov=True)

    #     image_path = "./images/images_2d/nora.jpeg"
    #     transform_image(image_path,frames=1,cleanup=True,make_mov=True)
    # except:
    #     print("something went wrong likely test files are missing")
         image_path = "./images/imageToSave.jpeg" 
         transform_image(image_path,frames=360,cleanup=True,make_mov=True,double=True)