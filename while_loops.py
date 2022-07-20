import random
#********************************************************************
 #                                                                  
 #  Team Edge Mini-project: WHILE LOOP CHALLENGES
 # 
 #   Complete the following loop challenges below. Follow the ToDos
 #   1. IN YOUR PRIME: Declare a while loop that prints all the prime 
 #      numbers between 0 and 100 (use the helper function provided)
 #   2. FOUND: use a while loop to search the contents of a list for
 #     the key!
 #   3. BUGGIN: Find out why these while loops don't do what they say 
 #     they do.
 #   4. MATH QUIZ: Prompt a user to solve a random math problem, if 
 #      they get it right, say congrats, if not, keep prompting.
 #   5. WHAT AM I: Write a game loop that prompts that never stops
 #      asking, "Iknow you are a _____, but what am I?"
 # 
 # ***************************************************************/

print("------------------- CHALLENGE 1 : IN YOUR PRIME -------------------")

#Here is a humble while loop in action. We need a variable to hold the counter value.
num = 0
while num <= 10:
    print("example counter--> " + str(num))
    num += 1


#------------ Helper function, do not mess with this part below ---------------??

def test_prime(n):
  if n==1:
    return False

  elif n == 2:
    return True

  else:
    for x in range(2, n-1):
      if n % x == 0:
        return False
    return True

#-->TODO: Declare a while loop that prints all the prime numbers between 0 and 100, use test_prime() helper function
num = 0

while num <= 100:
    if test_prime(num):
      print(num)
    num += 1


print("------------------- CHALLENGE 2 : FOUND   -------------------")

#here is a list full of items
items = ["pencil" , "eraser" , "mirror" , "comb" , "spoon" , "key" , "earrings" ,"cat food" , "magazine"]

#-->TODO: Use a while loop to search the contents of a list for the key! If it exists, print "found the key!"

active = True
while active:
  content = items.pop(0)
  if content == 'key':
    print(content)
    print('I FOUND THE KEY!')
    active = False
  else:
    print(content)


print("------------------- CHALLENGE 3 : BUGGIN   -------------------")

#Oh no! these functions have loops that don't do what they say they should do. Can you fix that?
#One more thing...to stop an infite loop you hit Control + C in the terminal  

#-->TODO: Make me count  2, 4, 6,..., 50

def even_numbers_to_fifty():
    num = 0
    while num < 50:
        num += 2
        print("number: " + str(num))

even_numbers_to_fifty()

#-->TODO: Make this design  below
#
#          [ 0 ]
#          [ 0, 1 ]
#          [ 0, 1, 2 ]
#          [ 0, 1, 2, 3 ]
#          [ 0, 1, 2, 3, 4 ]
#          [ 0, 1, 2, 3, 4, 5 ]
#          [ 0, 1, 2, 3, 4 ]
#          [ 0, 1, 2, 3 ]
#          [ 0, 1, 2 ]
#          [ 0, 1 ]
#          [ 0 ]



def pattern():

    index = 0 
    my_list =[]
    
    while index <= 5:
        my_list.append(index)
        print(my_list)
        index += 1

    index -= 1

    while index > 0:
        my_list.pop(index)
        print(my_list)
        index -= 1

pattern()


print("------------------- CHALLENGE 4 : MATH QUIZ   -------------------")
#-->TODO: Make a Math Quiz that asks two random numbers (between 0 and 100 to make it easy).
#         The user enters the answer. If wrong, keep prompting. If correct, say congrats!!
#         Use this handy boolean to get you started! You will need input()!

is_correct = False
ans = str(random.randint(0, 100))

while not is_correct:
  user_guess1 = input('Pick your first number: ').lower()
  user_guess2 = input('Pick your second number: ').lower()

  if user_guess1 == ans or user_guess2 == ans:
    print('Correct answer! You guessed it!')
    print('The answer was ', ans)
    is_correct = True
  elif user_guess1 == 'exit' or user_guess2 == 'exit':
    print('The answer was ', ans)
    is_correct = True
  else:
    print('Wrong answer! Keep guessing.')


print("------------------- CHALLENGE 5 : WHAT AM I?   -------------------")

#-->TODO: Write a game loop that prompts that never stops asking, "I know you are a _____, but what am I?"
#         You are given two starter functions and a loop to get started! 
#         Notice how one function calls the other and uses the returned value as the input. This is called Recursion! 

# keep_asking = True

# def prompt_user():
#     user_input = response(response)
#     user_input = input("I know you are a _____, but what am I? >> ")
#     return user_input

# def response(response):
#     print(f"I know you are a {user_input}, but what am I? >> ")
#     prompt_user()

# user_input = '_____'
# while keep_asking:
#   response(prompt_user())




#couldn't figure it out so i made my own

# user_input = '_____'
# while keep_asking:
#   user_input = input('I know you are a ' + user_input + ', but what am I? >> ').lower()
  
#   if user_input == 'exit':
#     keep_asking = False
    

#-->TODO: Challenge! write a secret word to break out of the loop!




