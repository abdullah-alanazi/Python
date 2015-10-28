import os
import pickle

def green_pickle(n,a,c):
	func = fi()
	info = (n , a , c)
	func = list(func)
	func.append(info)
	func = tuple(func)
	file1 = open('infoF.txt', 'wb')
	try:
		pickle.dump(func , file1)
	finally:
		file1.close()
# read from file
def fi():
	if (os.path.exists('infoF.txt')):
		filez = open('infoF.txt', 'rb')
		func = pickle.load(filez)
		filez.close()
	else:
		func =()
	return func


n = input("Enter a name :\t")
a = input("Enter the age:\t")
c = input("Enter the country:\t")
green_pickle(n,a,c)
func = fi()
print(" Data in pickle \n")
for i in func:
	print("The Info ::: ", i ,':::')
