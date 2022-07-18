# ********************************************************************

#  Team Edge List Miniproject: THE SHOPPING LIST HELPER

# This project prompts users using input() to prompt users
# to add (or remove) items from a\shopping list. It starts empty
# and each time the program is run it asks you to either add or 
# remove an item from the list. It also updates the user of its
# contents. The shopping list also checks to see if an item 
# is already present in the list and prevents you from adding it
# again, giving feedback along the way. -

# ***************************************************************

# active = True

# print("Welcome to Shopping List!")

# welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

# print(welcome_message)


#-->Todo: declare a shopping_list list


# def prompt_user():

#     reply = input("What do you want to add or remove?  >>  ")

#     return reply

# def check_answer(ans):
#     pass


# def add_item():

# # this function can take in a string and store it in an array
#     pass


# def remove_item():
#     pass

# while active:

#     check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True

# Gonna try making my own >:c
# --------------------------------------------------
def print_mylist():
    print('\n-------My List-------')
    print(mylist)
    print('--------------------- \n')



commands= '----------Commands---------- \nType add or remove, then your item to make changes to the list. \nType replace, to replace an item. \nType sort to sort your list alphabetically. \nType exit or checkout to leave the list. \nAnd type cmds to check the commands. \n---------------------------- \n'
active = True
mylist = [] 

print('Smart Shopping List here, what do you wish to do today? \n')
print(commands)


while active:
    confirming = True
    replacing = True
    user_input = input('What do you want to do? >> ').lower()
    user_cmd = 0


    if user_input != "":
        user_input = user_input.split()
        user_cmd = user_input.pop(0)
        user_input = " ".join(user_input)


    if user_cmd == 'add':
        if user_input in mylist:
            print('--Item is already in the list-- \n')
        elif user_input not in mylist and user_input != "":
            mylist.append(str(user_input))
            print_mylist()
        elif user_input == "":
            print('--There is nothing to add-- \n')

    elif user_cmd == 'remove':
        if user_input not in mylist:
            print("--Item doesn't exist-- \n")
        elif user_input in mylist:
            mylist.remove(str(user_input))
            print_mylist()
    

    elif user_cmd == 'replace' and len(mylist) != 0:
        while replacing:
            print_mylist()
            item1 = input('What is the item you want to change?  ').lower()
            
            if item1 in mylist:
                item2 = input('What is the item you want to add? ').lower()
                if item2 not in mylist and item2 != "":
                    item_position = mylist.index(item1)
                    mylist.remove(item1)
                    mylist.insert(item_position, item2)
                    print('Changes Made to List')
                    print_mylist()
                    replacing = False
                elif item2 == "":
                    print('--There is nothing to add-- \n')
                else:
                    print('--Item is already in the list--')
            else:
                print("--Item doesn't exist-- \n")


    elif user_cmd == 'replace' and len(mylist) == 0:
        print("--There's nothing in the list for you to replace, please add some items to your list first-- \n")


    elif user_cmd == 'sort':
        mylist.sort()
        print_mylist()
    

    elif user_cmd == 'exit' or user_cmd == 'checkout':
        while confirming:
            confirmed = input("Are you sure?(Yes or No): ").lower()
            print('\n')
            if confirmed == 'yes':
                active = False
                confirming = False
                items_amount = str(len(mylist))
                print('Items: ' + items_amount)
                print('The items you checked out are: ')
                print(mylist)
                print('Thank you for using this program.')
            elif confirmed == 'no':
                confirming = False
            else:
                print('--Please Try Again, Type Only Yes or No-- \n')
    

    elif user_cmd == 'cmds':
        print(commands)


    else:
        print('--Cannot Understand Your Command, Please Try Again-- \n')


    

