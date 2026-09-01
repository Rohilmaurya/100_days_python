import random

# ASCII Art for the hand gestures
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Map index/choices to the corresponding artwork
choices_art = [rock, paper, scissors]
choices_text = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")

while True:
    # 1. Get and validate user input
    user_input = input("Type 0 for Rock, 1 for Paper, 2 for Scissors (or 'q' to quit): ").lower().strip()
    
    if user_input == 'q':
        print("Thanks for playing!")
        break
        
    if user_input not in ['0', '1', '2']:
        print("Invalid choice. Please enter 0, 1, 2, or q.")
        continue
        
    user_choice = int(user_input)
    
    # 2. Generate computer choice
    computer_choice = random.randint(0, 2)
    
    # 3. Print the selections using ASCII art
    print("\nYou chose:")
    print(choices_art[user_choice])
    
    print("Computer chose:")
    print(choices_art[computer_choice])
    
    # 4. Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!\n")
    else:
        print("You lose!\n")
