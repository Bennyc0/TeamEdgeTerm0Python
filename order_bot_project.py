import random
# Food Order Bot

#Functions
def print_menu():
	
	drinks_menu = "---Drinks--- \n1. Water---$1.50 \n2. Soda---$1.50 \n3. Iced Tea---$2.00 \n4. None \n"
	meals_menu = "---Meals--- \n1. Hamburger---$8.00 \n2. Fried Rice---$9.00 \n3. None \n"
	sides_menu = "---Sides--- \n1. French Fries---$2.50 \n2. Chicken Nuggets---$2.50 \n3. None \n"
	desserts_menu = "---Desserts--- \n1. Ice Cream---$4.00 \n2. Chessecake---$4.00 \n3. None \n"
	
	menu_help = input("Type menu if you need the menu, otherwise press enter: ").lower()
	print('\n')

	if menu_help == 'menu':
		print(drinks_menu)
		print(meals_menu)
		print(sides_menu)
		print(desserts_menu)

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

def tip_calc():
	if tip_input == 0:
		return 0
	elif tip_input != int:
		print('Invalid Percentage, Automatically Making Tip 20% ')
		return subtotal*0.20
	elif int(tip_input) >= 1:
		return subtotal*0.01*int(tip_input)
	else:
		print('Invalid Percentage, Automatically Making Tip 20% ')
		return subtotal*0.20

#--------------------------------------------------

# Menu---Costs
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

print_menu()

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


subtotal = order_calc()
if offer2 == 'yes' and subtotal >= 12:
	subtotal = subtotal-4

if subtotal > 0:
	print("Please type in any number or else the tip will automatically be 20%")
	tip_input = input('How much do you want to tip? Please type in a number: ')
	print('\n')
else:
	tip_input = 0

tip = round(tip_calc(), 2)
tax  =  round(subtotal*0.08875, 2)
total = round(subtotal+tax+tip, 2)

print('Here is Your Reciept.\n')
print(f'Drink: {drink} \nMeal: {meal} \nSide: {side} \nDessert: {dessert} \n')

if offer1 == 'yes' and drink_order == '2' and meal_order == '1' and side_order == '1':
	print('You bought Soda, Hamburger, and French Fries together. You got a $4 off! \n')
elif offer2 == 'yes' and subtotal >= 12:
	print('You bought items worth $12 or more. You got a $4 off!')

print(f'Subtotal:${subtotal} \nTax:${tax} \nTip:${tip} \nTotal:${total} \n')

if total == 0:
	print("Thank you for using me. But please order something next time. 🥹")
else:
	print('Thank you for using this order bot, please come by again.')