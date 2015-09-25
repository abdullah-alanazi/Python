def bunnyEars(bunnies):
	if(bunnies == 0):
		return 0
	if(bunnies % 2 == 1):
		return 2 + bunnyEars(bunnies-1)
	return 3 + bunnyEars(bunnies-1)

a = 1987
while (a > 0):
	b_number = int(input("Please Enter the number of bunnies : "))
	print ("bunnyEars(", str(b_number), ") ->", bunnyEars(b_number))
#______________________________________________________________
#| 0u7pu75                                                     |
#|-------------------------------------------------------------|
#|   abdullahs-MacBook-Pro:desktop abdullah$ python3 hw3p1.py  |
#|   Please Enter the number of bunnies : 0                    |
#|   bunnyEars( 0 ) -> 0                                       |
#|   Please Enter the number of bunnies : 1                    |
#|   bunnyEars( 1 ) -> 2                                       |
#|   Please Enter the number of bunnies : 2                    |
#|   bunnyEars( 2 ) -> 5                                       |
#|   Please Enter the number of bunnies : 3                    |
#|   bunnyEars( 3 ) -> 7                                       |
#|_____________________________________________________________/

#   aBaDy
