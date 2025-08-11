import random

CLASSES = [
    "Warrior",
    "Paladin",
    "Cleric",
    "Wizard",
    "Rogue",
    "Shaman",
    "Necromancer",
    "Magician",
    "Ranger",
    "Bard",
]

RACES = [
    "Human",
    "Elf",
    "Dwarf",
    "Halfling",
    "Gnome",
    "Half-Orc",
    "Tiefling",
    "Dragonborn",
    "Goblin",
    "Aasimar",
]

RACE_STATS = {
    "Human": {"Dex": 10, "Str": 10, "Con": 10, "Wis": 10, "Int": 10, "Cha": 10},
    "Elf": {"Dex": 12, "Str": 8, "Con": 8, "Wis": 10, "Int": 12, "Cha": 10},
    "Dwarf": {"Dex": 8, "Str": 12, "Con": 12, "Wis": 10, "Int": 8, "Cha": 8},
    "Halfling": {"Dex": 12, "Str": 8, "Con": 10, "Wis": 10, "Int": 10, "Cha": 12},
    "Gnome": {"Dex": 10, "Str": 8, "Con": 10, "Wis": 10, "Int": 12, "Cha": 10},
    "Half-Orc": {"Dex": 8, "Str": 14, "Con": 12, "Wis": 8, "Int": 6, "Cha": 6},
    "Tiefling": {"Dex": 12, "Str": 8, "Con": 10, "Wis": 10, "Int": 12, "Cha": 14},
    "Dragonborn": {"Dex": 8, "Str": 12, "Con": 12, "Wis": 10, "Int": 8, "Cha": 10},
    "Goblin": {"Dex": 14, "Str": 8, "Con": 8, "Wis": 8, "Int": 10, "Cha": 6},
    "Aasimar": {"Dex": 10, "Str": 10, "Con": 10, "Wis": 12, "Int": 10, "Cha": 14},
}


def calculate_ac(stats):
    """Base armor class derived from Dexterity."""
    return 10 + stats["Dex"]


def attack(attacker, defender_ac):
    """Resolve a single attack against the given armor class."""
    roll = random.randint(1, 20)
    if roll + attacker["Dex"] >= defender_ac:
        return max(1, attacker["Str"] // 2)
    return 0


def combat(player_stats, enemy_stats, enemy_name="Goblin"):
    """Very simple combat loop using stats as attributes."""
    player_hp = player_stats["Con"] * 2
    enemy_hp = enemy_stats["Con"] * 2
    player_ac = calculate_ac(player_stats)
    enemy_ac = calculate_ac(enemy_stats)
    round_no = 1
    while player_hp > 0 and enemy_hp > 0:
        print(f"\n-- Round {round_no} --")
        dmg = attack(player_stats, enemy_ac)
        if dmg:
            enemy_hp -= dmg
            print(f"You hit the {enemy_name} for {dmg} damage! {enemy_name} HP: {max(enemy_hp, 0)}")
        else:
            print("You miss!")
        if enemy_hp <= 0:
            break
        dmg = attack(enemy_stats, player_ac)
        if dmg:
            player_hp -= dmg
            print(f"The {enemy_name} hits you for {dmg} damage! Your HP: {max(player_hp, 0)}")
        else:
            print(f"The {enemy_name} misses!")
        round_no += 1
    if player_hp > 0:
        print(f"\nYou defeated the {enemy_name}!")
    else:
        print(f"\nYou were defeated by the {enemy_name}...")


def get_choice(options, prompt):
    print(prompt)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    choice = input("Enter number or type your own: ")
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(options):
            return options[idx]
        else:
            print("Invalid number. Defaulting to custom input.")
    return choice.strip() or options[0]


def main():
    print("Welcome, traveler! The realm of Taldoria awaits your legend.\n")
    character_class = get_choice(CLASSES, "Choose your character class:")
    race = get_choice(RACES, "\nChoose your race:")
    stats = RACE_STATS.get(race, RACE_STATS["Human"])
    print("\nYour attributes:")
    for attr, value in stats.items():
        print(f"{attr}: {value}")
    print(f"\nYou have created a {race} {character_class}! Adventure begins now!")

    enemy = RACE_STATS["Goblin"]
    combat(stats, enemy, enemy_name="Goblin")


if __name__ == "__main__":
    main()
