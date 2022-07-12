import random
# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 

# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------

# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------

# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------

# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 

# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 

# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------

# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
#Menu
#Easier to read like this
drinks_menu = "---Drinks--- \n1. Water---$1.50 \n2. Soda---$1.50 \n3. Iced Tea---$2.00 \n4. None \n"
meals_menu = "---Meals--- \n1. Hamburger---$8.00 \n2. Fried Rice---$9.00 \n3. None \n"
sides_menu = "---Sides--- \n1. French Fries---$2.50 \n2. Chicken Nuggets---$2.50 \n3. None \n"
desserts_menu = "---Desserts--- \n1. Ice Cream---$4.00 \n2. Chessecake---$4.00 \n3. None \n"

# Costs
# 1. water = 1.50
# 2. soda = 1.50
# 3. iced_tea = 2.00

# 1. hamburger = 8.00
# 2. fried_rice = 9.00

# 1. french_fries = 2.50
# 2. chicken_nuggets = 2.50

# 1. ice_cream = 4.00
# 2. cheesecake = 4.00

# ?. none = 0

discount_offer = random.randint(1, 10)
offer1 = 'no'
offer2 = 'no'


print("Hello there. Welcome to my order bot.")
if discount_offer == 1 or discount_offer == 2:	
	print('\nLimited Offer: $4 off when you buy hamburger, french fries, and soda together! \n')
	offer1 = 'yes'
elif discount_offer == 3 or discount_offer == 4:
	print('\nLimited Offer: You get $4 off if you buy $12 or more! \n')
	offer2 = 'yes'
else:
	print('\nSorry, theres no offers for you today. \n')

menu_help = input("Type 'menu' if you need the menu, otherwise press enter: ")

if menu_help == 'menu':
	print(drinks_menu)
	print(meals_menu)
	print(sides_menu)
	print(desserts_menu)


drink_order = input('What drink would you like? Please type in the number: ')
meal_order = input('What meal would you like? Please type in the number: ')
side_order = input('What side would you like? Please type in the number: ')
dessert_order = input('What dessert would you like? Please type in the number: ')
print('\n')

if drink_order == '1':
	drink = 'Water---$1.50'
elif drink_order == '2':
	drink = 'Soda---$1.50'
elif drink_order == '3':
	drink = 'Iced Tea---$2.00'
else:
	drink = 'Nothing'

if meal_order == '1':
	meal = 'Hamburger---$8.00'
elif meal_order == '2':
	meal = 'Fried Rice---$9.00'
else:
	meal = 'Nothing'

if side_order == '1':
	side = 'French Fries---$2.50'
elif side_order == '2':
	side = 'Chicken Nuggets---$2.50'
else:
	side = 'Nothing'

if dessert_order == '1':
	dessert = 'Ice Cream---$4.00'
elif dessert_order == '2':
	dessert = 'Cheesecake---$4.00'
else:
	dessert = 'Nothing'


def order_calc():
	#drinks
	if drink_order == '1':
		drink_cost = 1.50
	elif drink_order == '2':
		drink_cost = 1.50
	elif drink_order == '3':
		drink_cost = 2.00
	elif drink_order == '4':
		drink_cost = 0
	else:
		print('Invalid Input, No Costs Calculated for Drinks \n')
		drink_cost = 0
	

	#meals
	if meal_order == '1':
		meal_cost = 8.00
	elif meal_order == '2':
		meal_cost = 9.00
	elif meal_order == '3':
		meal_cost = 0
	else:
		print('Invalid Input, No Costs Calculated for Meals \n')
		meal_cost = 0


	#side
	if side_order == '1' or side_order == '2':
		side_cost = 2.50
	elif side_order == '3':
		side_cost = 0
	else:
		print('Invalid Input, No Costs Calculated for Sides \n')
		side_cost = 0
	

	#dessert
	if dessert_order == '1' or dessert_order == '2':
		dessert_cost = 4.00
	elif dessert_order == '3':
		dessert_cost = 0
	else:
		print('Invalid Input, No Costs Calculated for Desserts \n')
		dessert_cost = 0

	
	#offer
	if offer1 == 'yes' and drink_order == '2' and meal_order == '1' and side_order == '1':
		drink_cost = 1.50
		meal_cost = 4.00
		side_cost = 2.50

	return drink_cost+meal_cost+side_cost+dessert_cost

subtotal = order_calc()
if offer2 == 'yes' and subtotal >= 12:
	subtotal = subtotal-4
# --------------------------------------

print('Please type in a proper percentage, or else it will automatically be 10%.\n')
tip_input = input('How much percentage do you want to tip?(Type 5, 10, 15, 20, or 25): ')
print('\n')

def tip_calc():
	if tip_input == '5':
		return subtotal*0.05
	elif tip_input == '10':
		return subtotal*0.1
	elif tip_input == '15':
		return subtotal*0.15
	elif tip_input == '20':
		return subtotal*0.2
	elif tip_input == '25':
		return subtotal*0.25
	else:
		print('Invalid Percentage, Automatically Making Tip 10% ')
		return subtotal*0.15

tip = round(tip_calc(), 2)
tax  =  round(subtotal*0.08875, 2)
total = round(subtotal+tax+tip, 2)

print('Here is Your Reciept.\n')
print(f'Drink:{drink} \nMeal:{meal} \nSide:{side} \nDessert:{dessert} \n')

if offer1 == 'yes' and drink_order == '2' and meal_order == '1' and side_order == '1':
	print('You bought Soda, Hamburger, and French Fries together. You got a $4 off! \n')
elif offer2 == 'yes' and subtotal >= 12:
	print('You bought items worth $12 or more. You got a $4 off!')

print(f'Subtotal:${subtotal} \nTax:${tax} \nTip:${tip} \nTotal:${total} \n')
print('Thank you for using this order bot, please come by again.')