# check_age_validation.py
while True:
	age = input("Your age: ")
	if not age.isdigit():
		print("Invalid input. Please enter a number.")
	else:
		age = int(age)
		if age < 13:
			print("You are a child.")
		if 13 <= age < 18:
			print("You are a teenager.")
		if age >= 18:
			print("You are an adult.")
