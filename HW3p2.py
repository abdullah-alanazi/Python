def count_frequency( alist ):
	dictionary = {}
	for i in alist:
		if i  in list(dictionary.keys()):
			dictionary [i] += 1
		else:
			dictionary.update({i:1})
	return dictionary
mylist=["one","two","eleven","one","three","two","eleven","three","seven","eleven"]
print (count_frequency(mylist))
#-------------------------------------------------------------
#   0u7pu7
#_____________________________________________________________
#   abdullahs-MacBook-Pro:desktop abdullah$ python3 hw3p2.py |
#   {'seven': 1, 'eleven': 3, 'three': 2, 'one': 2, 'two': 2}|
#------------------------------------------------------------/

#     aBaDy
