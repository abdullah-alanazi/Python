user= input('Enter the path and file name: \n')
insidF =open(user, 'r')
trust= 'password='
count=0 
for  digit,line in enumerate(insidF):
	if line.find(trust)!= -1:
		print('The line is ',digit ,': The password is:-\n', line[:])
		count+=1
s= count
if s <=0:
	print (user ,' is SECUR.')
if s >=1:
	print (user, ' is NOT SECURE.')
#--------------------------------------------------------------
#--------------------------------------------------------------
#       output
#--------------------------------------------------------------
# abdullahs-MacBook-Pro:~ abdullah$ cd desktop
# abdullahs-MacBook-Pro:desktop abdullah$ python3 hw4-2.py
# Enter the path and file name: 
# pass.txt
# The line is  2 : The password is:-
#   password= 19871505 
#
# pass.txt  is NOT SECURE.
#--------------------------------------------------------------
