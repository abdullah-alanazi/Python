
class Animal:
	AList = {"elephant": ("\033[33;3mI have exceptional memory\033[0m", "\033[33;3mI am the largest land-living mammal in the world\033[0m", "\033[33;3myou can play with me in India & I've a long noise ^_*\033[0m"), 
				"tiger": ("\033[33;3mI am the biggest cat\033[0m", "\033[33;3mI come in black and white or orange and black\033[0m", "\033[33;3mI'm living in jungles\033[0m "), 
				"bat": ("\033[33;3mI use echo-location\033[0m", "\033[33;3mI can fly\033[0m", "\033[33;3mI see well in dark\033[0m")}

	def __init__(self, Xanimal):
		self.Xanimal = Xanimal

	def guess_who_am_i(self):
		c= 0
		print("\033[31;1mI will give you 3 hints, guess what animal I am\033[0m")

		while (True):
			if (c < 3):
				print (Animal.AList[self.Xanimal][c])
				X = input("\033[35;7mWho am I?:\033[0m ").lower()
				if X != self.Xanimal:
					print ("\n\033[35;7mNope, try again!\033[0m\n")
					c +=1
				else:
					print("\n\033[35;7mYou got it! I am ", X)
					break
			else:
				print("\033[35;7mI'm out of hints! The answer is:\033[0m", self.Xanimal)
				break

e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
