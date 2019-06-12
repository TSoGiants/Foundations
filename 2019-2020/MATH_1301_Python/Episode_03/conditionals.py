name = input("Please enter your name. > ")

print("Hello, " + name.split(" ")[0].title() + "!")

x = input("Give me an integer to add: ")

try:
	x = int(x)	
except:
	print("The value you entered is not a number.")
else:
	y = input("Give me another integer to add: ")
	try:
		y = int(y)	
	except:
		print("The second value you entered is not a number.")
	else:
		print("The sum of your numbers is: " + str(x + y))