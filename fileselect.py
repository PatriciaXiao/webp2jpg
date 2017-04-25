import os

def list_only_files(path):
	onlyfiles = [ f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
	return onlyfiles