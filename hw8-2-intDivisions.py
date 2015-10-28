from random import randrange
print('INTEGER DIVISIONS')
for i in range(8):
	a = randrange(5)
	b = randrange(5) * a
	if ((a != 0 and b == 0) or (a != 0 and a > b)):
		a,b = b,a
	try:
			ans = int(input(str(b)+"/"+str(a)+"="))
			if (ans == b//a):
				print("CORRECT")
			else:
				print("INCORRECT")
	except ValueError:
				print("Please enter integers only!")
	except Exception as e:
				print("Err0r ")
				print(type(e))
