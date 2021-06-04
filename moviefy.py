# import os

# orignially was going down the native ffmpeg route ###

####

# def moviefy(unique_id,image_name):
#     os.system("ffmpeg -framerate 10 -i testimages/hopeitworks%03d.png -s:v 1280x720 \
#         -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p" + str(unique_id) + ".mp4")

#####

import os
import glob
from moviepy.editor import *

def moviefy(unique_id,image_name,frames,audio=True):
    base_dir = os.path.realpath('./images/images_effected/'+ str(unique_id)+"/" )
    # print(base_dir)

    fps = 24

    file_list = glob.glob('./images/images_effected/'+ str(unique_id)+'/'+ '*.png')  # Get all the pngs in the current directory
    
    file_list_sorted = sorted(file_list,reverse=False)  # Sort the images
    # print()
    # print(file_list_sorted)
    # print()
    clips = [ImageClip(m).set_duration(1/24)
            for m in file_list_sorted]
    # print(clips)
    if audio != None:
        concat_clip = concatenate_videoclips(clips, method="compose")
        video_with_new_audio = concat_clip.set_audio(AudioFileClip("./images/sounds/clip1.wav")) 
        video_with_new_audio.write_videofile(image_name + ".mp4", fps=fps,audio_codec='aac')
    else:
        concat_clip = concatenate_videoclips(clips, method="compose")
        concat_clip.write_videofile(image_name + ".mp4", fps=fps,)



# moviefy("7b67b9cf-bace-431d-8796-3afe095bec8c","image") #for testing