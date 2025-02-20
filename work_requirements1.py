# Decided to do all 10 of them :)
## Simply run the code, and then select which exercise to check out in the input (1 to 10)

# Easier navigation between exercises
exercise = input("Enter an Exercise Number: ")
exercise = int(exercise)


# Exercise 1 - Greeting and Age Check
if(exercise == 1):
    print("You are checking out Exercise 1!, Greeting and Age Check")

    # Prompts to get Name and Age
    user_name = input("Hello! what is your name? ")
    user_age = input("May i ask you how old you are? ")

    # Converting age from string to integer
    user_age = int(user_age)

    # If User are 18 or above they can enter, otherwise they are too young
    if(user_age >= 18):
      print("Greetings! ", user_name, " You are old enough to enter!")
    else:
        print("Sorry", user_name, " you are too young")
    


# Exercise 2 - Number List Processor
## Went abit further with this one, where setting control if user is setting number 0 or 10
elif(exercise == 2):
	print("You are checking out Exercise 2!, Number List Processor")

	# User will give an number
	provide_number = input("Hello! Give a number from 1 to 10: ")
    # Made number from String to Integer
	provide_number = int(provide_number)
      
	# Will contain a list of numbers
	list_of_numbers = []

	# User typed 11 or more
	if(provide_number > 10):
		print("Number was a tad high, please give a number 1 - 10. The number you gave were: ", provide_number)

	# User tried to be cheeky typing 0
	elif(provide_number < 1):
		print("Number was too low, an 0 i suspect. Please try again")

	# It passed and are an number 1 to 10,
    ## Now on each iteration a number from 1 to the number user gave will be placed into the list.
	else:
		for number in range(1, provide_number + 1):
			list_of_numbers.append(number)

	# Showing the list of numbers
	print("List of numbers from 1 to", provide_number, "are:", list_of_numbers )

	# If list is 6 or more in length, then it is a long list
	if(len(list_of_numbers) > 5):
		print("The List is long!")

	# Otherwise it is a short one
	else:
		print("The list is short")



# Exercise 3 - Sum of User Inputs
elif(exercise == 3):
	print("You are checking out Exercise 3!, Sum of User Inputs")

	# Get the three numbers from the user
	number_one = input("Enter a number: ")
	number_two = input("Enter another number: ")
	number_three = input("Enter a third number: ")

	# Convert the strings to integers
	number_one = int(number_one)
	number_two = int(number_two)
	number_three = int(number_three)

	# Find the Total and print it out
	total = number_one + number_two + number_three
	print(total)

	# Checking if the sum is even or odd through modulus (if anything is left after dividing by 2)
	if(total % 2 == 0):
		print("Your sum is even!")
	else:
		print("Your sum is odd!")



# Exercise 4 - Fruit Basket
elif(exercise == 4):
	print("You are checking out Exercise 4!, Fruit Basket")

	# Created a dictionary with some fruits and how many of them are in stock
	fruit_basket = { "apple": 10, "banana": 5, "peach": 7, "orange": 3, "grape": 100 }

	# Asking the user for a fruit
	state_your_fruit = input("I heard you like fruits! Check which fruits we got in the store! Enter a fruit: ")

	# If fruit is in the dictionary, it will print the amount of that fruit in stock, aswell as spelling each letter of it.
	if(state_your_fruit in fruit_basket):
		print("We have that fruit in stock!", fruit_basket[state_your_fruit], "of them to be exact!")
		# Displays each letter of the fruit to a new line
		for fruit_letter in state_your_fruit:
			print(fruit_letter)
	else:
		print("We don't have that fruit in stock!")



# Exercise 5 - Temperature Converter
elif(exercise == 5):
	print("You are checking out Exercise 5!, Temperature Converter")

	# Asking the user to enter a temperature in Celsius
	celsius_given = input("Enter a temperature in Celsius: ")
	celsius_given = float(celsius_given)

	# Converting Celsius to Fahrenheit - Found documentation: https://en.wikipedia.org/wiki/Celsius#Coexistence_with_Kelvin
	## It takes celcius and multiplies it by 9 / 5, then adds 32 to get the fahrenheit
	fahrenheit = (celsius_given * 9/5) + 32
	# Show the temperature in Fahrenheit
	print("The temperature in Fahrenheit is:", fahrenheit)

	# By the Fahrenheit temperature, it will tell you if it is hot or not
	if(fahrenheit > 80):
		print("It is hot!")
	else:
		print("It is not too hot.")

	# Placed the temperatures of each kind in a list, and printed it out.
	temperatures_list = [celsius_given, fahrenheit]
	print("Here are the temperatures in a list:", temperatures_list)



# Exercise 6 - Menu Selection
elif(exercise == 6):
	print("You are checking out Exercise 6!, Menu Selection")

	# A dictionary with menu items and their prices
	menu_items = {"coffee": 30, "tea": 20, "juice": 25}

	# Asking the user to select a menu item
	menu_selection = input("Select a menu item: ")

	# If item is found, then a print of the item and the price will be shown - Otherwise it will say it is not found
	if(menu_selection in menu_items):
		print("You selected", menu_selection, "which costs", menu_items[menu_selection])
		
	else:
		print("Item not found in the menu!")

	# Display a full list of the menu items
	print("This is what we currently have on the menu: ")
	for item, price in menu_items.items():
		print(item, price)



# Exercise 7 - Number Analyser
## Note: Could easily use Min, Max and Sum to find the numbers, but task said using a loop
elif(exercise == 7):
	print("You are checking out Exercise 7!, Number Analyser")

	# Instructional message
	print("Please enter only numbers separated by spaces (for example, 20 5 59 10). No commas or letters!")

	# Get user input
	get_numbers = input("Enter numbers: ")
	# Split input into a list of strings
	string_numbers = get_numbers.split()
	# Create an empty list to store the integers
	numbers_list = []

	# Converting each of the string number into an integer and then i add it to the list
	for number in string_numbers:
		numbers_list.append(int(number))

	# Printing the final list, with all the numbers
	print("These are the numbers you typed:", numbers_list)

	# Setting up the variables, to display smalles, largest and average number
	## Each of these two, begins at the very first number in the list
	smallest_number = numbers_list[0]
	largest_number = numbers_list[0]

	# Will be the total amount, to use for the average sum
	total_sum = 0

	# Looping through the number list, to find the smallest, largest and total sum.
	for number in numbers_list:
		# If number is smaller than the previous number set
		if number < smallest_number:
			smallest_number = number
		# If number is larger than the previous number set
		if number > largest_number:
			largest_number = number
		# Simply adding the number to the sum of the previous one
		total_sum += number

	# Calculate the average number
	average = total_sum / len(numbers_list)

	# Print the results for smallest, largest and average sum
	print("Smallest number is:", smallest_number)
	print("Largest number is:", largest_number)
	print("Average value is:", average)

	# Checking if the average is high or low
	if average > 10:
		print("Average is high.")
	else:
		print("Average is low.")



# Exercise 8 - Letter Counter
## Bubble is a word that can show that it works :)
elif(exercise == 8):
	print("You are checking out Exercise 8!, Letter Counter")

	word_from_user = input("Enter a word: ")

	# Make the word to lowercase - Found documentation here: https://www.programiz.com/python-programming/methods/string/lower
	word_from_user = word_from_user.lower()
	print("You entered the word:", word_from_user)

	# Empty Dictionary to take each letter
	letter_counts = {}

	# For every iteration, go through each of the letters in the word. 
	for letter in word_from_user:
		# If letter exist, add +1 to it
		if letter in letter_counts:
			letter_counts[letter] += 1
		# If Letter do NOT exist, add 1 to it
		else:
			letter_counts[letter] = 1

	# Showing how many times an letter was mentioned in the word. 
	print("Letter counts:", letter_counts)

	# If word is longer than 5 then print that it is so
	if len(word_from_user) > 5:
		print("That's a long word!")



# Exercise 9 - Guessing Game
elif(exercise == 9):
	print("You are checking out Exercise 9!, Guessing Game")
	print("Guess the secret number: 1 - 10! Best of luck! :) ")

	# Define your secret number here
	secret_number = 7

	# Had to define variable before using it within the loop
	guessed_number = None

	# Will contain all the guesses user made
	all_guesses = []

	# Will run as long as the guessed number are not matching the secret number
	while secret_number != guessed_number:

		# Making user ask a number, and then converting it to an integer
		guessed_number = input("Guess the number: ")
		guessed_number = int(guessed_number)

		# No matter if right or wrong, it will be appended to the list
		all_guesses.append(guessed_number)

		# Correct number was made and user will see all their guesses!
		if(guessed_number == secret_number):
			print("You guessed it!")
			print("here is all your guesses! - ", all_guesses)
			break

		# User need to guess again
		else:
			print("try again")



# Exercise 10 - Shopping List Manager
elif(exercise == 10):
	print("You are checking out Exercise 10!, Shopping List Manager")

	# Creating an empty shopping list
	shopping_list = []

	# Used to track if user is done or not - Boolean
	is_done = False

	# To be sure user know that writing done "end" adding to the list
	print("Type done, once you are done adding things to the list")

	# Will run as long as user dont type Done
	while(is_done != True):

		# Prompt to have user add to the shopping list
		add_to_shopping_list = input("Add an item to your shopping list! ")

		# If user write done, the loop ends.
		## Made sure that no matter how user write DoNe it will end, by making it lowercase
		if add_to_shopping_list.lower() == 'done':

			# Prints the entire shopping list
			print("Here are the items in your shopping list: ", shopping_list)
			
			# Simply give a message based on the amount of items added to the list
			if len(shopping_list) > 3:
				print("You have a lot of items!")
			else:
				print("You have a short list")
			break

		# User just added something to the list, so we add it, and user can add another
		else:
			shopping_list.append(add_to_shopping_list)
			print(add_to_shopping_list, " Have been added to the list")


# User tried to enter a number that is not on the list
else:
	print("No Exercise found for that Input")