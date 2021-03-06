import numpy as np
from scipy import ndimage

import imageutils as iutils

def prepareImg(filename, height=50, filter_radius=8, invert=False, compress=False):
	"""prepare image for mapping to stl file"""
	img = None
	if filename[-5:] == '.fits':
		f = fits.open(filename)
		for hdu in f:
			if isinstance(hdu.data, np.ndarray):
				img = hdu.data
				break
		f.close()
	else:
		img = iutils.img2array(filename)
	# legacy below
	# if crop != False:
	# 	img = iutils.crop_image(img, crop) if np.isscalar(crop) else iutils.crop_image(img, 1.0)
	# 	if np.isscalar(crop):
	# 		img = remove_background(img, crop)
	# 	else:
	# 		img = remove_background(img, 1.0)
	if compress and img.shape[0] > 500:
		img = iutils.compressImage(img, 500)
	if filter_radius:
		# print("here3")
		img = ndimage.filters.gaussian_filter(img, filter_radius)
	# print(img)
	img = img - img.min()
	# print(img)
	if invert:
		img = img.max() - img
	img = iutils.normalize(img, True, height)
	return np.fliplr(img)
















