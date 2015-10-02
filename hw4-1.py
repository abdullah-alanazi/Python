import fnmatch
import os
rootpath = input(" Enter the inital path : ")
fileN = input (" Enter the file name : ")
for rootp,dirs,files in os.walk(rootpath):
	for f in fnmatch.filter(files,fileN):
		print("Found at : ",os.path.join(rootp,f))
