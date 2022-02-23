import random
import time
split = "--------------------------"
red = "\u001b[31m"
green = "\u001b[32m"
white = "\u001b[37;1m"
reset = "\u001b[0m"
four_letters = [
"spin",
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
"file",
"pest",
"quit",
"heir",
"thaw",
"main",
"duck",
"door",
"weed",
"swim",
"care",
"play",
"bend",
"wing",
"pool",
"soft",
"deer",
"rape",
"nose",
"grip",
"sign",
"park",
"harm",
"fear",
"fall",
"slam",
"node",
"plug",
"ring",
"slow",
"dorm",
"mile",
"rain",
"veil",
"film",
"hurl",
"dash",
"boot",
"gasp",
"hike",
"gold",
"golf",
"bear",
"bean",
"burn",
"like",
"look"
]



final_fours = list(set(four_letters))
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
    """elif choice == 2:
      word = random.choice(final_fives)
      total = 5
    elif choice == 3:
      word = random.choice(final_sixes)
      total = 6"""
    
    guesses = 0
    underscores = ['_ ' for _ in range(total)]
    while guesses < 5:
      guess = input(f"Please guess the word: {''.join(underscores)} ")
      for count, value in enumerate(guess):
        if value in word[count]:
          underscores[count] = value
      guesses = guesses + 1
      if guess == word:
        break

    print(split)
    if guess == word:
      print(f"Congrats! The word was {word}. It took you {guesses} of 5 guesses to get right.")
    elif guess != word:
      print(f"Sorry, you didn't get the word. The word was {word}.")
    print("Do you wish to play again?")
    print("1 | Yes \n2 | No")
    play = int(input())
    if play == 1:
      play = True
      print(f"\nRestarting script...\n{split}\n\n\n\n")
    elif play == 2:
      play = False
print("Ok then. Bye!")
print("--- END OF FILE ---")
time.sleep(5)
