import random
words = [
    "apple", "beach", "chair", "dance", "earth", "fruit", "ghost", "happy", "juice", "lemon",
    "animal", "bridge", "castle", "dragon", "forest", "guitar", "island", "monkey", "orange", "planet",
    "blanket", "chimney", "diamond", "elephant", "feather", "galaxy", "hammer", "igloo", "jungle", "kangaroo",
    "lantern", "magnet", "needle", "octopus", "puzzle", "quartz", "rocket", "spider", "telescope", "umbrella",
    "vampire", "window", "xylophone", "yacht", "zebra", 
    "awkward", "bagpipes", "crypt", "dwarves", "jukebox", "oxygen", "rhythm", "sphinx", "unknown", "zealous", 
    "jazz", "buzz", "frizz", "fluff", "gypsy", "hajj", "mnemonic", "phlegm", "queue", "zucchini"
]
random_word = random.choice(words)
print("Welcome to Hangman!")
guessed_letters = []
attempts = 6
while attempts > 0:
    guess=input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    if guess in random_word:
        print("Correct guess!")
    for letter in random_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
         
    if guess not in random_word:
        attempts -= 1
        print(f"\nIncorrect guess! You have {attempts} attempts left.")
    if attempts == 0:
        print(f"\nGame over! The word was '{random_word}'.")
    if all(letter in guessed_letters for letter in random_word):
        print(f"\nCongratulations! You've guessed the word '{random_word}' correctly!")

        

        

