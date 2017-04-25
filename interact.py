import sys
import re
from importlib import import_module
import traceback
import platform
import copy

class color:
	COLOR_PLATFORMS = ['Darwin', 'Linux']
	if platform.system() in COLOR_PLATFORMS:
		BLUE = '\033[94m'
		GREEN = '\033[92m'
		YELLOW = '\033[93m'
		RED = '\033[91m'
		ENDC = '\033[0m'
	else:
		OKBLUE, OKGREEN, WARN, FAIL, ENDC = '', '', '', '', ''
	COLOR_MAP = {
		"blue": BLUE,
		"green": GREEN,
		"yellow": YELLOW,
		"red": RED
	}


def color_text(text_content, text_color=None):
	if text_color in color.COLOR_MAP:
		return color.COLOR_MAP[text_color] + text_content + color.ENDC
	else:
		return text_content

def check_input(input_string, expect):
	if len(input_string) > 0 and input_string[0] in expect:
		return True
	return False