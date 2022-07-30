#sorry about the bad organization, didn't bother organizing it but at least the code works.
import random
from time import sleep

delay = 1
completion = "False"
cmds = "Type 'go' then the area's name that you want to go to move there. \nType 'look' to see the information of the area you are currently in. \nType 'mystats' to check your profile. \nType 'talk' then the npc's name you want to talk with to talk with them. \nType 'fight' then the enemy's name to fight them. \nType 'help' to see the commands again. \n"
game_hints = ["Hint: You can answer the questions some npcs ask", "Hint: 'Letter'"]
notes = "Note: BTW, I ordered the move options in fighting from lowest damage to highest(Higher damage = Less accuracy). \nNote2: Talk To The Npcs! \nNote3: PLEASE STOP TRYING TO FIGHT EVERY NPC YOU SEE!!! \nNote4: Make sure to 'look'! \n"

# ----------NPCs----------
class NPC:
    def __init__(self, name, description, dialogue, health, damage):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.health = health
        self.damage = damage
        self.move = ["punches", "kicks", "headbutts"]

        if self.name == "head knight":
            self.move = ["slashes", "slices", "cuts", "stabs", "counters"]

    def __repr__(self):
        return f'\n{self.dialogue}'

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        while self.is_alive() and enemy.is_alive():
            self_move = random.choice(self.moves)
            enemy.health = round(enemy.health - self.damage)


# ----------Enemies----------
class Enemy:
    def __init__(self, name, discription, dialogue, health, damage):
        self.name = name
        self.discription = discription
        self.dialogue = dialogue
        self.health = health
        self.damage = damage
        self.move = ["slashes", "slices", "cuts", "stabs", "counters"]

    def __repr__(self):
        return f"\n{self.discription} \n{self.dialogue} \n"

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        while self.is_alive() and enemy.is_alive():
            self_move = random.choice(self.moves)
            enemy.health = round(enemy.health - self.damage)


# ----------Player----------
class Player:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.health = 100
        self.damage = 0
        self.accuracy = 0
        self.move = None

    def __repr__(self):
        return f"\nName: {self.name} \nItems in inventory: {self.items} \nHealth: {self.health} \n"

    def is_alive(self):
        return self.health > 0

    def move_selection(self):
        global select_move
        active = True

        while active:
            if "sword" in player.items:
                move_type = input(
                    "Do you wish to use sword attacks or melee attacks?(You can just type 'sword'(s) or 'melee'(m))>> ")
                if "melee" in move_type or "sword" in move_type or move_type == "s" or move_type == "m":
                    pass
                else:
                    print("--<Unable to understand your selection>-- \n")
            else:
                move_type = "melee"

            if "melee" in move_type or move_type == "m":
                print(melee_attacks_list)
                select_move = input("Which move do you wish to use?>> ")
                print("\n")
                for attack in melee_attacks_dict:
                    if select_move == attack:
                        attack = melee_attacks_dict.get(attack)
                        self.damage = attack.accuracy_check()
                        return attack.name
                        active = False

            elif "sword" in move_type or move_type == "s":
                print(sword_attacks_list)
                select_move = input("Which move do you wish to use?>> ")
                print("\n")
                for attack in sword_attacks_dict:
                    if select_move == attack:
                        attack = sword_attacks_dict.get(attack)
                        self.damage = attack.accuracy_check()
                        return attack.name
                        active = False

    def block_check(self):
        if select_move == "block" or select_move == "sword block":
            return True
        else:
            return False

    def attack(self, enemy):
        print(f"{self.name}'s hp: {self.health} \n{enemy.name}'s hp: {enemy.health} \n")

        while self.is_alive() and enemy.is_alive():
            active = True
            self.move = self.move_selection()
            enemy_move = random.choice(enemy.move)

            if self.block_check():
                self.damage = 0
                block_chance = random.randint(0, 15)

                while active:
                    player_guess = input(" \nPlease guess a number(0-15): ")
                    if player_guess.isdigit():
                        if int(player_guess) >= block_chance - 2 and int(player_guess) <= block_chance - 2:
                            block_percent = 100
                            print("\n --<Perfect Block!>-- \n")
                            active = False

                        elif int(player_guess) >= block_chance - 3 and int(player_guess) <= block_chance + 3:
                            block_percent = 5
                            perfect_block = False
                            print("\n --<Good Block!>-- \n")
                            active = False

                        elif int(player_guess) >= block_chance - 5 and int(player_guess) <= block_chance + 5:
                            block_percent = 3
                            print(f"{self.name} uses {self.move}. {self.name} is ready to block some damage. \n")
                            active = False

                        else:
                            print("\n --<Block Failed!>-- \n")
                            block_percent = 1
                            active = False
                    else:
                        print("--<Please enter a whole number from 0 to 15>-- \n")

            else:
                if self.damage > 0:
                    enemy.health = round(enemy.health - self.damage)
                    print(f"{self.name} used {self.move} and dealt {self.damage} damage to {enemy.name}!")

                else:
                    print(f"{self.name} used {self.move}. The {self.move} missed!")

                print(f"{self.name}'s hp: {self.health} \n{enemy.name}'s hp: {enemy.health} \n")

            if self.is_alive() and enemy.is_alive():
                if select_move == "block" or select_move == "sword block":
                    if block_percent == 100:
                        print(f"{self.name} excuted a Perfect Block! The {enemy.name}'s weapon went flying! The {enemy.name} needs time to recover their weapon.")
                        print(f"{self.name}'s hp: {self.health} \n{enemy.name}'s hp: {enemy.health} \n")
                        use_hp_pot = input("Do you want to take this chance to use a hp potion?(Yes or No)>> ").lower()

                        if "yes" in use_hp_pot:
                            self.health = self.health + 30
                            print(" \n--<You gained 30  more health!>-- \n")
                            print(f"{self.name}'s hp: {self.health} \n{enemy.name}'s hp: {enemy.health} \n")
                        else:
                            print(f" \n--<You decide to not use the chance to drink a hp pot>-- \n")

                    elif block_percent == 1:
                        self.health = round(self.health-enemy.damage/block_percent)
                        print(f"The {enemy.name}'s {enemy_move} did {round(enemy.damage/block_percent)} damage.")

                    else:
                        self.health = round(self.health-enemy.damage/block_percent)
                        print(f"{self.name} used {self.move}! The {enemy.name}'s {enemy_move} did {round(enemy.damage/block_percent)} damage.")
                        print(f"{self.name}'s hp: {self.health} \n{enemy.name}'s hp: {enemy.health} \n")

                else:
                    self.health = round(self.health-enemy.damage)
                    print(f"{enemy.name} {enemy_move} {self.name} for {enemy.damage} damage!")
                    print(f"{self.name}'s hp: {self.health} \n{enemy.name}'s hp: {enemy.health} \n")

        if self.is_alive():
            print("--<You Won!>-- \n")
            for enemies in enemy_dict:
                if enemy.name.lower() == enemies:
                    enemies = enemy_dict.get(enemies)
                    current_area.enemies.remove(enemies.name.lower())

            for npc_enemies in npc_dict:
                if enemy.name.lower() == npc_enemies:
                    npc_enemies = npc_dict.get(npc_enemies)
                    current_area.npcs.remove(npc_enemies.name.lower())

        else:
            print("--<You Lost!>-- \n")


class Player_attack:
    def __init__(self, name, description, min_damage, max_damage, accuracy):
        self.name = name
        self.description = description
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.accuracy = accuracy

    def __repr__(self):
        return (f"\nAttack Name: {self.name} \nAttack Description: {self.description} \nAttack Damage: {self.damage} Damage \nAttack Accuracy: {self.accuracy}% \n")

    def random_damage(self):
        random_dmg = random.randint(self.min_damage, self.max_damage)
        return random_dmg


    def accuracy_check(self):
        random_number = random.randint(0, 100)

        if self.accuracy <= random_number:
            self.damage = 0
            return self.damage
        else:
            self.damage = self.random_damage()
            return self.damage
    


# ----------Places----------
class Area:
    def __init__(self, name, description, npcs, enemies, paths):
        self.name = name
        self.description = description
        self.npcs = npcs
        self.enemies = enemies
        self.paths = paths

    def __repr__(self):
        return (f"Area: {self.name} \nDescription: {self.description} \nNpcs: {self.npcs} \nEnemies: {self.enemies} \nPaths: {self.paths} \n")


# ----------The Database----------
# ---npcs---
west_gate_guards = NPC("West Gate Guards", "Two armoured guards stand guard with their spears at the gate.", "Guard: This gate is closed. Try the north or the east gate.", 80, 10)
south_gate_guards = NPC("South Gate Guards", "Two armoured guards stand guard with their spears at the gate.", "Guard: This is area is closed due to landslides in the area. It will take a few days before it's open again.", 80, 10)
north_gate_guards = NPC("North Gate Guards", "Two armoured guards stand guard with their spears at the gate.", "Guard: There has been bandit sightings recently. You should bring a sword with you, if you do't have one, go get one from the blacksmith. Take care out there!", 80, 10)
east_gate_guards = NPC("East Gate Guards", "Two armoured guards stand guard with their spears at the gate.", "Guard: There has been bandit sightings recently. You should bring a sword with you, if you do't have one, go get one from the blacksmith. Take care out there!",80, 10)
citizen1 = NPC("Worried Lady", "A lady that has a very worried expression on her face.", "Lady: Theres a rumor going around that bandits are going to attack the city. I hope it's not true...", 50, 3)
citizen2 = NPC("Busy Merchant", "A merchant unloading his boxes of wares from his cart.", "Merchant: Quit blocking my path! I gotta get these boxes unloaded.", 50, 3)
blacksmith = NPC( "Working Blacksmith","A blacksmith hammering away on his unfinished sword.","Blacksmith: Hm? What are you doing here? Are you here for the sword?", 50, 5)
grassyfields_sheep = NPC("A Sheep", "A sheep eating its grass and enjoying the weather","Sheep: BAAAAAAAA!", 10, 1)
wounded_traveler = NPC("Traveler", "A heavily wounded traveler.","Traveler: TAKE this letter and GIVE it to the head knight in the city for me please. I won't be able to make it with these injuries. Also, whatever you do, don't go into the forest. \n--<Type 'take letter' to take the letter>--", 25, 1)
head_knight = NPC("Head Knight", "The head of the knights of the city.", "Head Knight: ...", 125, 15)

npc_dict = {
    "west gate guards": west_gate_guards,
    "south gate guards": south_gate_guards,
    "north gate guards": north_gate_guards,
    "east gate guards": east_gate_guards,
    "citizen1": citizen1,
    "citizen2": citizen2,
    "blacksmith": blacksmith,
    "sheep": grassyfields_sheep,
    "traveler": wounded_traveler,
    "head knight": head_knight
}

# ---bandits---
bandit_alone = Enemy("Bandit", "--<A bandit with a cloak appeared>--", "Bandit: MWAHAHAHAHA- DIE!!!", 100, random.randint(5, 10))
bandit_pair = Enemy("Bandit Pair", "--<2 wild bandits appeared!>--","Bandits: HAND OVER YOUR MONEY NOW!",random.randint(40, 55), random.randint(5, 10))
bandit_group = Enemy("Bandit Group", "--<A group of wild bandits appeared!>--","Bandits: Take your pick, life or money?",random.randint(80, 100), random.randint(10, 15))
bandit_army = Enemy("Bandit Army", "--<An army of wild bandits appeared!>--","DIE INTRUDER!", 250, 20)
bandit_leader = Enemy("Bandit Leader",  "--<The boss of the wild bandits has appeared!>--",  "You shouldn't had come here...", 100, 30)
# bandit alone is supposed to be not fightable

enemy_dict = {
    "bandit alone": bandit_alone,
    "bandit pair": bandit_pair,
    "bandit group": bandit_group,
    "bandit army": bandit_army,
    "bandit leader": bandit_leader,
}

# ---player attacks---
heavy_slash = Player_attack("Heavy Slash", "A heavy slash using your sword. Does high damage, but is very slow and easy to evade.", 30, 40, 40)
sword_pierce = Player_attack("Sword Pierce", "A piercing attacking with your sword. Requires high precision or you will miss the weakspots.", 30, 35, 50)
sword_slice = Player_attack("Sword Slice", "A slicing attack using your sword. It it very weak, but is easy to use and hit your target.", 10, 15, 95)
# sword_parry = Player_attack("Sword Parry", "A hard defensive technique that allows to you prevent an enemy attack landing on you. You also reflect most damage.", round(enemy_move*4/5), 70)
# sword_counter = Player_attack("Sword Counter", "A defensive technique that allows you to reflect partial damage to your enemy.", round(enemy_move*2/5), 90)
sword_block = Player_attack("Sword Block", "A basic defensive technique that blocks and prevents most damage.", 0, 0, 100)
#nerfing sword blocks, cant have the player blocking and then attacking while enemy is "stunned", scratch the original plan.
#parry and counter are WIP, might not be finished and used.

punch = Player_attack("Punch", "The most basic of the basic melee attacks.",  5, 10, 100)
uppercut = Player_attack("Uppercut", "A low punch that goes upwards.", 12, 18, 80)
down_chop = Player_attack("Downwards Chop", "A chopping attack. You chop your enemies hard on the head with this. They are going to be seeing stars.", 20, 25, 70)
low_kick = Player_attack("Low Kick", "A kick that gets them almost everytime.", 10, 15, 90)
roundhouse_kick = Player_attack("Roundhouse Kick", "A semicircular kick, striking the enemy with your leg. Easy to evade but hits hard.", 30, 40, 60)
block = Player_attack("Block", "Blocks your enemy's attack with your arms. Gonna hurt, even with armor on.", 0, 0, 100)
#accuracy system is used to balance out the game. Attack selection will be pointless without different damage, can't have the player picking strongest attack everytime.

sword_attacks_list = ["sword block", "sword slice", "sword pierce", "heavy slash"]
melee_attacks_list = ["block", "punch", "low kick", "uppercut", "down chop", "roundhouse kick"]

sword_attacks_dict = {
    "heavy slash": heavy_slash,
    "sword pierce": sword_pierce,
    "sword slice": sword_slice,
    "sword block": sword_block
}

melee_attacks_dict = {
    "punch": punch,
    "uppercut": uppercut,
    "down chop": down_chop,
    "low kick": low_kick,
    "roundhouse kick": roundhouse_kick,
    "block": block
}

# ---areas---
city_square = Area("City Square", "The center of the city.", ["citizen1", "citizen2", "head knight"], [], ["city smithy", "city west gate", "city south gate","city north gate", "city east gate"])
city_smithy = Area("City Smithy", "Your local blacksmith.", ["blacksmith"], [],["city square"])
city_west_gate = Area("City West Gate", "The west gate of the city.",["west gate guards"], [], ["city square"])
city_south_gate = Area("City South Gate", "The south gate of the city.",["south gate guards"], [], ["city square"])
city_north_gate = Area("City North Gate", "The north gate of the city.",["north gate guards"], [], ["city square", "grassy fields"])
city_east_gate = Area("City East Gate", "The east gate of the city.",["east gate guards"], [],["city square", "grassy fields"])
grassy_fields = Area("Grassy Fields ","The lush green fields to the east of the city. There's a fork in the path leading to north and south Redwood Forest.",["sheep"], [],["city east gate", "grassy fields northeast", "grassy fields southeast"])
grassy_fields_northeast = Area("Grassy Fields Northeast","The path that goes to the north of the Redwood Forest.", ["traveler"],["bandit pair"], ["redwood forest north", "grassy fields"])
grassy_fields_southeast = Area("Grassy Fields Southeast","The path that goes to the south of the Redwood Forest.", [],["bandit group"], ["grassy fields", "redwood forest south"])
redwood_forest_north = Area("Redwood Forest North","Northern parts of the Redwood Forest.", [],["bandit army", "bandit leader"], [])
redwood_forest_south = Area("Redwood Forest South", "Southern parts of the Redwood Forest.", [], [],["grassy fields southeast", "deeper redwood forest"])
bandit_camp = Area("Deeper Redwood Forest","The camp bandits had made in the Redwood Forest.", [],["bandit army", "bandit leader"], [])

area_dict = {
    "city square": city_square,
    "city smithy": city_smithy,
    "city west gate": city_west_gate,
    "city south gate": city_south_gate,
    "city north gate": city_north_gate,
    "city east gate": city_east_gate,
    "grassy fields": grassy_fields,
    "grassy fields northeast": grassy_fields_northeast,
    "grassy fields southeast": grassy_fields_southeast,
    "redwood forest north": redwood_forest_north,
    "redwood forest south": redwood_forest_south,
    "deeper redwood forest": bandit_camp
}

# ----------GameSystems----------
# ---function---
def fight(a, b):
    a.attack(b)
    b.attack(a)


# ---player system--
def start():
    global player
    global current_area

    active = True
    current_area = city_square

    print("--<Hello Player>-- \n")
    print("This is your last few days of in this city. After this week, your summer vacation ends and you have to go back home for middle school. \n\nYou decide that you want to explore the Redwood forest that is to the east of the city. \n")

    while active:
        player_name = input("What is your name, player?>> ")

        if player_name.strip():
            print("--<Processing name...>-- \n")
            sleep(delay)
            confirm = input(f"Name accepted! Your name is {player_name}, correct?(Yes or No)>> ").lower()

            if confirm == "yes":
                print(f"Ok! \nWelcome {player_name}! \n\n")
                active = False
        else:
            print("--<Could not understand. Try again>-- \n")
            sleep(delay)

    print(cmds)
    print(notes)
    player = Player(player_name, [])


# ---game system---
def prompt_player():
    active = True
    while active:
        reply = input("What do you want to do?>> ").lower()
        if reply.strip():
            reply = reply.split()

            return reply
            active = False
        else:
            print("--<Cannot be blank>-- \n")


def player_command(input):
    global current_area
    global completion

    print("--<Processing input...>-- \n")
    sleep(delay)

    # "go"
    if "go" in input:
        if len(input) >= 2:
            if len(current_area.enemies) == 0:
                new_area1 = input[-2] + " " + input[-1]
                if len(input) >= 3:
                    new_area2 = input[-3] + " " + input[-2] + " " + input[-1]

                for matching_area in current_area.paths:
                    if new_area1 == matching_area or new_area2 == matching_area:
                        current_area = area_dict.get(matching_area)
                        print("You are now at " + current_area.name + "\n")
                        print(current_area)

            else:
                print("--<Please fight the enemies in the area first!(If there is an enemy in the [], also don't include the [] or the '')>--")
        else:
            print("--<Please state the area you want to go to after 'go'>--")

    # "look"
    elif "look" in input:
        print(f"You are at the {current_area}")

    elif "talk" in input:
        if len(input) >= 2:
            npc1 = input[-1]
            npc2 = input[-2] + " " + input[-1]
            npc3 = "Nothing"

            if len(input) >= 3:
                npc3 = input[-3] + " " + npc2

            for npc in current_area.npcs:
                if npc1 == npc or npc2 == npc or npc3 == npc:
                    interact_npc = npc_dict.get(npc)
                    print(interact_npc.description + "\n" +
                          interact_npc.dialogue + "\n")
                    if npc == "head knight" and "letter" in player.items and current_area == city_square:
                        print("--<Type 'give letter' to give the letter to head knight!>--")

        else:
            print("--<Please state the npc you want to talk with after 'talk'>--")

    elif "fight" in input:
        if len(input) >= 2:
            target1 = input[-1]
            target2 = input[-2] + " " + input[-1]
            for enemy in current_area.enemies:
                if target1 == enemy or target2 == enemy:
                    target = enemy_dict.get(enemy)
                    fight(player, target)
                else:
                    for npc_enemy in current_area.npcs:
                        if target1 == npc_enemy or target2 == npc_enemy:
                            target = npc_dict.get(npc_enemy)
                            fight(player, target)
        else:
            print("--<Please state the enemy you want to fight after 'fight'>--")

    elif "mystats" in input:
        print(player)

    elif "help" in input:
        print(cmds)

    #extra features:
    elif "yes" in input and current_area == city_smithy and "blacksmith" in city_smithy.npcs:
        player.items.append("sword")
        print("Blacksmith: Ok, hang on for a bit, im almost done with the sword. \n--<15 minutes later>-- \n")
        print(f"--<{player.name} obtained a sword!>--")

    elif input == ['take', 'letter'] and current_area == grassy_fields_northeast and "letter" not in player.items and "traveler" in grassy_fields_northeast.npcs:
        player.items.append("letter")
        print("The letter is addressed to the head knight of the city.")
        print(f"--<{player.name} obtained a letter!>--")
        head_knight = NPC("Head Knight", "The head of the knights of the city.", "Head Knight: How can I help you?", 125, 15)

    elif input == ['give', 'letter'] and current_area == city_square and "head knight" in city_square.npcs:
        player.items.remove("letter")
        print("--<You have successfully delivered the letter to the head knight>-- \n")
        completion = "True"

    else:
        print("--<Unable to understand your input, try again>-- \n")

    if current_area == bandit_camp or current_area == redwood_forest_north:
        print("--<You walked into the forbidden zone>-- \n")
        print("--<You get ambushed by the bandits>--")
        print("--<You prepare to fight them, knowing that you won't make it out alive>-- \n")
        for enemy in current_area.enemies:
            target = enemy_dict.get(enemy)
            fight(player, target)
            if player.is_alive():
                completion = "True"
                print("--<You beated the leader and his army that is supposed to be impossible>--")
                print("--<Secret Ending: Beating the Bandits>-- \n")


# ----------The Game----------

start()
while player.is_alive() and completion == "False":
    reply = prompt_player()
    player_command(reply)

if not player.is_alive():
    random_hint = random.choice(game_hints)
    print(" \n--<Game Over!>-- \n")
    print(random_hint)

if completion == "True":
    print("--<Congratulations, you beaten the game!🥳🥳>--")
    print("--<Wonder how many tries it took you to get here🤔>-- \n")
    attempts = input("How many tries did it take?>> ")

print("Thank you for playing.")
