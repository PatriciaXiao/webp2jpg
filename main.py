from fileio import *
from fileselect import *
from interact import *

import sys

# print color_text("hello world", "green")
# assert False, color_text("hello world", "red")
# python main.py "./data/fruit/" "./data/fruit_out/"
# python main.py "./data/flower/" "./data/flower_out/"
# python main.py "./data/moon/1/" "./data/moon_out/1"
# python main.py "./data/moon/2/" "./data/moon_out/2/"
# python main.py "./data/moon/3/" "./data/moon_out/3/"
# python main.py "./data/moon/4/" "./data/moon_out/4/"
# python main.py "./data/moon/5/" "./data/moon_out/5/"
# python main.py "./data/moon/6/" "./data/moon_out/6/"
# python main.py "./data/moon/7/" "./data/moon_out/7/"

def main():
	# get user input
	if len(sys.argv) != 3:
		print(color_text("warning: parameters do not match the format that we expected: main.py input_folder output_folder", text_color="yellow"))
		user_decision = raw_input("are you sure you still want to continue anyway? (Y/N)")
		if not check_input(user_decision, ['Y', 'y']):
			exit()
	try:
		input_folder = sys.argv[1]
		output_folder = sys.argv[2]
	except IndexError:
		print(color_text("error: please provide an input folder name and an output folder name", text_color="red"))
		print("example: main.py \"./input/\" \"./output/\"")
		exit()
	# get input files
	try:
		onlyfiles = list_only_files(input_folder)
		# print onlyfiles
	except OSError:
		print(color_text("error: the input folder given does not exist; please enter a valid directory", text_color="red"))
		exit()
	# deal with the webp files only
	webpfiles = [f for f in onlyfiles if f.endswith(".webp")]
	# print webpfiles
	# deal with each file separately
	cnt_files = len(webpfiles)
	cnt = 0
	for file in webpfiles:
		img = load_image(input_folder, file)
		file_name = file.split(".")[0]
		cnt += 1
		try:
			print("saving image {0}, processed ({1}/{2})".format(file_name + ".jpg", cnt, cnt_files))
			save_image(img, output_folder, file_name + ".jpg")
		except IOError:
			print(color_text("error: the output folder given does not exist; please enter a valid directory", text_color="red"))
			exit()

if __name__ == "__main__":
	main()