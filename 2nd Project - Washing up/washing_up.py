import random

print("=== Washing Up Chooser ===")
print("Let's decide who washes up today!\n")

#  Ask how many people
while True:
    try:
        num_people = int(input("How many people are there? (1-10): "))
        if 1 <= num_people <= 10:
            break
        else:
            print("Please enter a number between 1 and 10!")
    except ValueError:
        print("That's not a number! Please try again.")

#  Collect names
people = []

print(f"\nOkay! Please enter {num_people} name(s):")
for i in range(1, num_people + 1):
    while True:
        name = input(f"Person {i}: ").strip()
        if name:  
            people.append(name)
            break
        else:
            print("Please enter a name (can't be empty)!")

#  Choose random 
print("\nThinking...")
print("...drumroll...")
victim = random.choice(people)

#  Announce the result
print("\n" + "=" * 40)
print(f"   THE WASHING UP CHOSEN ONE IS...")
print("          ✨ " + victim.upper() + " ✨")
print("=" * 40)

print(f"\nSorry {victim}, it's your turn today! 🧼🍽️")
print("Good luck! 💪")
