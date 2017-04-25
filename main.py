from fileio import *
from fileselect import *
from interact import *

import sys

# print color_text("hello world", "green")
# assert False, color_text("hello world", "red")

def main():
	# get user input
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
	# deal with the webp files

if __name__ == "__main__":
	main()