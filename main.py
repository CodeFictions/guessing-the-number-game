import random
tries = 0
user_name = input("Enter your name:- ")
user_name.strip()

print(f"Hello {user_name}!")
print("Would you like to play Guess the number game?")
print("1) Yes")
print("2) No")
option = int(input("Select your option:- "))

if option == 1:
	lower = int(input("Enter the lower bound:- "))
	upper = int(input("Enter the higher bound:- "))
	number = random.randint(lower, upper)
	print(f"I am thinking a number in between {lower} and {upper}.")
	print("You have to guess the correct number in 3 tries")
	guess = int(input("Guess the number:- "))
	tries+=1
	if guess > number:
		print("Guess lower...")
	if guess < number:
		print("Guess higher...")
	while guess != number and tries < 3:
		guess = int(input("Try again: "))
		tries += 1
		if guess > number:
			print("Guess lower...")
		if guess < number:
			print("Guess higher...")
	if guess == number:
		print("You won!")
		print(f"Number of tries:- {tries}")
	else:
		print("You lost!")
		print(f"The number was {number}")
elif option == 2:
	print("Thank you!")
else:
	print("Invalid Option")