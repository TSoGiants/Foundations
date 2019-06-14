
while True:
	x = input("Give me an integer to add: ")
	try:
		x = int(x)	
	except:
		print("The value you entered is not a number.")
	else:
		while True: 
			y = input("Give me another integer to add: ")
			try:
				y = int(y)	
			except:
				print("The second value you entered is not a number.")
			else:
				print("The sum of your numbers is: " + str(x + y))
				break
		while True:
			status = input("Continue? (y/n) ")
			quit = False
			if status.lower() == "n" or status.lower() == "no":
				print("Thank you. Goodbye.")
				quit = True
				break
			elif status.lower() == "y" or status.lower() == "yes":
				print("Ok. Continuing.")
				break
			else:
				print("What?")
		if quit:
			break
		else:
			pass
