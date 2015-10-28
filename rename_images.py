#!/usr/bin/env python

import os
rootdir = os.getcwd()
for root, dirs, files in os.walk(rootdir):
	for directory in dirs:
		workingdir = os.path.join(root, directory)
		contents = os.listdir(workingdir)
		if '*.jpg' or '*.JPG' in contents:
			count = 1
			os.chdir(workingdir)
			for file in contents:
				if os.path.isfile(file):
					if file == '.DS_Store':
						os.remove(file)
					elif directory.lower() not in file or directory not in file:
						newfile =  directory + " " + str(count) + '.jpg'	 
						os.rename(file, newfile)
						count = count + 1 
	os.chdir(rootdir)
