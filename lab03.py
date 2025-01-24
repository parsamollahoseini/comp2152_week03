# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

# Use list() and range() to create dice options
diceOptions = list(range(1, 7))

# Display available weapons using a loop
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
print("Available Weapons:")
for index, weapon in enumerate(weapons, start=1):
    print(f"{index}. {weapon}")

# Validate player combat strength input
while True:
    try:
        combatStrength = int(input("Enter your combat Strength (1-6): "))
        if 1 <= combatStrength <= 6:
            break
        else:
            print("Input must be an integer between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Validate monster combat strength input
while True:
    try:
        mCombatStrength = int(input("Enter the monster's combat Strength (1-6): "))
        if 1 <= mCombatStrength <= 6:
            break
        else:
            print("Input must be an integer between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Battle simulation
print("\n--- Battle Begins! ---")
for round_num in range(1, 20, 2):  # Simulate 10 rounds (1, 3, 5...19)
    print(f"\nRound {round_num}:")
    
    # Roll dice for hero and monster
    hero_roll = random.choice(diceOptions)
    monster_roll = random.choice(diceOptions)
    
    # Determine weapons based on dice rolls
    hero_weapon = weapons[hero_roll - 1]
    monster_weapon = weapons[monster_roll - 1]
    
    # Add dice roll to combat strength
    hero_strength = combatStrength + hero_roll
    monster_strength = mCombatStrength + monster_roll
    
    # Announce round results
    print(f"Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {hero_strength}, Monster Total Strength: {monster_strength}.")
    
    # Determine round winner
    if hero_strength > monster_strength:
        print("Hero wins the round!")
    elif hero_strength < monster_strength:
        print("Monster wins the round!")
    else:
        print("It's a tie!")
    
    # Break condition for "Battle Truce"
    if round_num == 11:
        print("Battle Truce declared in Round 11. Game Over!")
        break

print("\n--- End of Battle ---")

