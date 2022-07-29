# -------------------------------------------- 
# Ignore this section. This is just for checking your work

def check_answers(gen_answer, correct_answer):
    if gen_answer == correct_answer:
        print("Your code works!")
    else:
	    print(f"Try again, your code generated {gen_answer} but the correct answer is {correct_answer}")

def add_numbers(x, y):
	return x+y

def sub_numbers(x, y):
	return x-y

def multiply_numbers(x, y):
	return x*y

def divide_numbers(x, y):
	return x/y

def calculator():
	active = True

	while active:
		print('Type exit to stop program.')
		operation = input('What do you want to do?(Add, Sub, Multiply, Divide): ').lower()

		if operation == 'exit':
			active = False
			print('\n')
		else:
			num1 = int(input('Enter any number: '))
			num2 = int(input('Enter any number: '))
		
			if operation == 'add':
				ans = add_numbers(num1, num2)
				print(f'The answer is {ans}. \n')

			elif operation == 'sub':
				ans = sub_numbers(num1, num2)
				print(f'The answer is {ans}. \n')

			elif operation == 'multiply':
				ans = multiply_numbers(num1, num2)
				print(f'The answer is {ans}. \n')

			elif operation == 'divide':
				ans = divide_numbers(num1, num2)
				print(f'The answer is {ans}. \n')

			else:
				print('Invalid Operation')

def sleep_time_calc():
	active = True
	sleep_start = int(input('Which hour do you go to sleep? Please type in numbers: '))
	sleep_end = int(input('Which hour do you wake up? Please type in numbers: '))

	while active:
		clock = input('What time do you wish to use? 12-hours to 24-hours:  ').lower()
		if clock == "12-hours":
			sleep_end = sleep_end+12
			return sleep_end-sleep_start
			active = False
		elif clock == "24-hours":
			return sleep_end-sleep_start
			active = False
		else:
			print('--Invalid clock--')

# -------------------------------------------- 

	# You've just learned all about functions. 
	# Now take what you've learned to create your own

					# CALCULATOR!

	# We'll guide you through the first few steps,
	# then you'll have a chance to add your own features
	# that will make this your new go-to calculator!

# -------------------------------------------- 

print("My Simple Calculator")

# -------------------------------------------- 

# Part 1: 

	# The first features of any simple calculator is that
	# it should be able to perform the basic math operations. 
	# Let's start by writing the functions we'll need to execute 
	# the following operations:

		# Addition
		# Subtraction

# -------------------------------------------- 
 
# Write a function called add_numbers that will take two numbers and return the sum.
# Write a function called sub_numbers that will take two numbers and return the difference.
# ------------
# Testing Code - Uncomment the code below to test your code!

check_answers(add_numbers(5, 15), 20)
check_answers(add_numbers(3, 18), 21)
check_answers(add_numbers(12, 28), 40)

check_answers(sub_numbers(18, 7), 11)
check_answers(sub_numbers(11, 9), 2)
check_answers(sub_numbers(18, 21), -3)

# -------------------------------------------- 

# Part 2: 

	# Now that you have addition and subtraction down, let's add the other operators we learned!

	# Finish off your basic calculator by writing the functions 
	# for the following operations:

		# Multiplication
		# Division 

# -------------------------------------------- 

# Write a function called multiply_numbers that will take two numbers and return the product.
# Write a function called divide_numbers that will take two numbers and return the quotient.
# ------------
# Testing Code - Uncomment the code below to test your code!

check_answers(multiply_numbers(10, 3), 30)
check_answers(multiply_numbers(21, 7), 147)
check_answers(multiply_numbers(4, 16), 64)

check_answers(divide_numbers(24, 100), .24)
check_answers(divide_numbers(21, 7), 3)
check_answers(divide_numbers(15, 4), 3.75)

# -------------------------------------------- 

# Part 3: 

	# Now that you have your basic functions in place, you need to get some user input.
	# What's a calculator for if no one is using it?

# Write a function that will prompt the user for the operation they want to call and the values they are inputting.

# -------------------------------------------- 
# -------------------------------------------- 

# Part 4: 

	# Now that you have all of the basic four operations completed, you get to add your own features!
	# What will you add to make this your go-to calculator? 

	# Stuck? : Think about what you count/calculate on a (almost) daily basis.
	# Can you write a function that will take in the data you need and do the calculation for you? 

	# (I know I calculate how many hours of sleep I get every day... ｡(*^▽^*)ゞ )

# -------------------------------------------- 

# Write a function or functions that will add some unique features to your calculator. 
# Don't forget to:
		# Give your function an name and parameters that are self explanatory and written in camelcase!
		# Use comments throughout your code
		# Test your code!
  
# -------------------------------------------- 
calculator()

use_sleep_calc = input('Do you wish to use the sleep calculator?(yes or no): ').lower()
if use_sleep_calc == 'yes':
	ans = sleep_time_calc()
	print(ans, 'hours of sleep time.')

	if ans <= 0:
		for_real = input('Did you put in the values correctly?(yes or no): ').lower()
		if for_real == 'yes':
			print('HOW CAN YOU EVEN GET NEGATIVE HOURS OF SLEEP!? \n')
		if for_real == 'no':
			print('Oh, I see. You scared me! \n')
	elif ans >= 12:
			print('Wake up lazybones, stop sleeping and get to work! \n')
	elif ans >= 24:
		print('YOU SHOULD REALLY GET OUT OF BED!!! \n')

else:
	print('Ok, thank you for using the simple calculator. \n')

#--------------Continuous Calculator----------------

def cont_calc():
	active = True
	numbers = []
	blank = '--Blank Input, Try Again--'

	while active:
		operation = input('What operation do you wish to use?(Add, Sub, Multiply, or Divide): ').lower()

		if operation.strip():
			if len(numbers) == 0:
				num_input = int(input('What number?: '))

		# ".strip" is used to check if input is either blank or just spaces
		if operation.strip():
			numbers.append(num_input)
			num1 = numbers.pop(0)
			num_input = int(input('What number?: '))
			if operation == 'add':
				result = add_numbers(num1, num_input)
				print(result)
				
			else:
				print(blank)
		else:
			print(blank)

print('Testing Phase: Continuous Calculator')
cont_calc()