import random
split = "--------------------------"

four_letters = ["spin",
"push",
"side",
"stop",
"hurl",
"feed",
"fade",
"lead",
"mail",
"seat",
"wire",
"cave",
"tent",
"duty",
"game",
"soap",
"blow",
"bear",
"slab",
"deny",
"fist",
"poem",
"full",
"meat",
"long",
"crop",
"mask",
"open",
"file"]



final_fours = list(dict.fromkeys(four_letters))
play = True
while play == True:
    print("Welcome to Wordle MK2 by Sean!")
    print(split)
    print("Please select your word length using the numbers on the left:\n")
    print("1 | 4 Letters.")
    print("2 | 5 Letters.")
    print("3 | 6 Letters.\n")
    print(split)
    choice = int(input())
    
    if choice == 1:
      word = random.choice(final_fours)
      total = 4
    """,elif choice == 2:
      word = random.choice(final_fives)
      total = 5
    elif choice == 3:
      word = random.choice(final_sixes)
      total = 6"""
    
    guesses = 0
    underscores = ['_' for _ in range(total)]
    
    while guesses < 6:
      guess = input(f"Please guess the word: {underscores}")
      for count, value in enumerate(guess):
        if value in word:
            underscores[count] = value
      guesses = guesses + 1
      if guess = word:
        break
      
    print(f"Congrats! The word was {word}. It took you {guesses} of 5 guesses to get right. Do you wish to play again?")
    print("1 | Yes \n2 | No")
    play = int(input())
print("Ok then. Bye!")
print("--- END OF FILE ---")