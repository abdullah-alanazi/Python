import shelve
from datetime import *
# my dictionary 
dic = {"abdullah": "abady","19871505":"start","x":(9,8,7,6,5,4,3,2,1) }
# shelve 
shlv = shelve.open("shlve")
shlv["abdullah"]= "abady"
shlv["19871505"]="start"
shlv["x"]=(9,8,7,6,5,4,3,2,1)
# dictionary operation
print("Dictionary :\n")
dt = datetime.now()
for x ,y in dic.items():
	print(x , ":::",y)
dt1 = datetime.now()
DictionaryTime = dt1-dt
# shelve operation
print("\nshElvE : \n")
DT = datetime.now()
for x ,y in shlv.items():
	print(x , ":::", y)
shlv.close()
DT1 = datetime.now()
ShelveTime= DT1 - DT 
# time operation
print("dictionary time : " , DictionaryTime)
print("shelve time : ", ShelveTime )
# organize
if ShelveTime > DictionaryTime:
	print ("dictionary is faster ")
elif ShelveTime < DictionaryTime:
	print("Shelve is faster ")
else:
	print("dictionary and shelve are same time processing ")
