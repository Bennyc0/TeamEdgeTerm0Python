import random

class Fighters:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def is_alive(self):
        self.health > 0
        return self.health > 0

    def attack(self, enemy):
        enemy.health = enemy.health-self.damage
        print(f"{self.name} does {self.damage} damage to {enemy.name}.")
        print(f"{self.name} has {self.health} health left. \n")

swordsman = Fighters("Swordsman", random.randint(5,20), random.randint(90,110))
goblin = Fighters("Goblin", random.randint(15,25), random.randint(50, 75))

print('A wild Goblin Appeared!')
print(f"Swordsman's health is {swordsman.health}")
print(f"Goblin's health is {goblin.health} \n")

while swordsman.is_alive() and goblin.is_alive():
    swordsman.damage = random.randint(5,20)
    goblin.damage = random.randint(15,25)
    swordsman.attack(goblin)
    goblin.attack(swordsman)

if goblin.is_alive():
    print('Game Over \n')
else:
    print('You Win \n')