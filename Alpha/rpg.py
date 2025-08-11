from Player import Player
import random

# Simple Enemy class (you can split this out later too)
class Enemy:
    def __init__(self, name="Goblin", hp=20, attack_range=(3, 6)):
        self.name = name
        self.hp = hp
        self.attack_range = attack_range

    def attack(self, target):
        dmg = random.randint(*self.attack_range)
        target.hp -= dmg
        print(f"{self.name} attacks {target.name} for {dmg} damage!")

# Create player and enemy
player = Player()
enemy = Enemy()

# Game loop
while player.hp > 0 and enemy.hp > 0:
    print(f"\n{player.name} HP: {player.hp} | Potions: {player.potions}")
    print(f"{enemy.name} HP: {enemy.hp}")
    action = input("Choose an action: [A]ttack, [P]otion: ").lower()

    if action == "a":
        player.attack(enemy)
    elif action == "p":
        player.use_potion()
    else:
        print("Invalid input!")

    if enemy.hp > 0:
        enemy.attack(player)

# End of battle
if player.hp <= 0:
    print("You were defeated!")
else:
    print(f"You defeated the {enemy.name}!")