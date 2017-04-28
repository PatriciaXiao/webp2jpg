from PIL import Image
import os

def load_image(path, name, FORMAT="RGB"):
	fullname = os.path.join(path, name)
	im = Image.open(fullname).convert(FORMAT)
	return im

def save_image(im, path, name, FORMAT="jpeg"):
	fullname = os.path.join(path, name)
	im.save(fullname, FORMAT)
	pass