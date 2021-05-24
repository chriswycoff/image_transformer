
import sys

from imageprep import prepareImg
from meshcreator import to_mesh

# if __name__ == '__main__':
# 	if len(sys.argv) != 3:
# 		print("Usage: ./img2stl <path_to_image> <new_stl_filename>")
# 	img = prepareImg(sys.argv[1])
# 	to_mesh(img, sys.argv[2], depth=1, double=False, _ascii=False)

def make_stl(img_file, new_file, depth=1, double=False, _ascii=False):
	img = prepareImg(img_file)
	to_mesh(img, new_file, depth=depth, double=double, _ascii=_ascii)