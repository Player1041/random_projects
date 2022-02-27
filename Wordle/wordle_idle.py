import sys
import random
import time
import sys

try:
    colour = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

split = "--------------------------"

black = "SYNC"
green = "STRING"
orange = "KEYWORD"


four = ['wash', 'mark', 'stun', 'flee', 'dink', 'exam', 'mind', 'pals', 'bake', 'kill', 'beef', 'baba', 'oath', 'pees', 'void', 'suds', 'dung', 'rows', 'node', 'baba', 'bark', 'feet', 'gain', 'lump', 'hide', 'bowl', 'sump', 'neck', 'oven', 'soot', 'mask', 'cows', 'toga', 'temp', 'glad', 'pled', 'sofa', 'lobe', 'grim', 'felt', 'zone', 'tosh', 'male', 'gall', 'dock', 'pose', 'prom', 'fort', 'conk', 'thug', 'were', 'west', 'gage', 'pick', 'calm', 'deer', 'turn', 'mugs', 'duly', 'cuts', 'casa', 'flow', 'duty', 'near', 'soul', 'bulk', 'pops', 'aide', 'fans', 'chug', 'liar', 'crow', 'deaf', 'bite', 'clop', 'lame', 'dump', 'loon', 'fame', 'hugs', 'gout', 'moll', 'body', 'rats', 'vine', 'dewy', 'down', 'drab', 'very', 'clad', 'duty', 'brit', 'mind', 'skin', 'pods', 'boot', 'stag', 'farm', 'wrap', 'font']

five = ['stark', 'catch', 'buses', 'ralph', 'halls', 'quest', 'virus', 'lusts', 'heels', 'welsh', 'nacho', 'truer', 'rants', 'piper', 'rapid', 'pesky', 'lunar', 'upper', 'taxes', 'heavy', 'heaps', 'mount', 'poles', 'laser', 'upset', 'blond', 'pools', 'gemma', 'fixed', 'birds', 'couch', 'thick', 'baton', 'slack', 'deity', 'pains', 'climb', 'mills', 'rhino', 'wacko', 'luton', 'hedge', 'peels', 'smile', 'brill', 'talks', 'lures', 'goods', 'hello', 'churn', 'heals', 'props', 'privy', 'snarl', 'quack', 'fails', 'dined', 'swell', 'flank', 'repay', 'tummy', 'elect', 'blues', 'guide', 'prick', 'parts', 'genes', 'party', 'manly', 'armor', 'poles', 'wheat', 'coral', 'goons', 'outdo', 'moons', 'proms', 'shall', 'smith', 'ariel', 'rocky', 'swiss', 'smith', 'meats', 'rehab', 'waltz', 'cures', 'upset', 'reset', 'viper', 'soars', 'gusto', 'floor', 'paint', 'lambs', 'crank', 'motto', 'crush', 'vroom', 'vicar']

six = ['steady', 'remind', 'skimpy', 'thorpe', 'smacks', 'hitter', 'counts', 'jammer', 'shakes', 'ailing', 'fibber', 'velvet', 'looked', 'mouths', 'salami', 'easter', 'upbeat', 'dumped', 'deeper', 'lethal', 'marble', 'lilacs', 'benign', 'supply', 'barter', 'blurry', 'decker', 'weaker', 'target', 'rectal', 'delude', 'verbal', 'rubber', 'smacks', 'drools', 'spoons', 'graham', 'jazzed', 'visual', 'pearly', 'staged', 'sabers', 'lenses', 'napkin', 'libido', 'hiking', 'critic', 'direct', 'louder', 'rapids', 'curses', 'paying', 'pleads', 'glassy', 'waiter', 'drafts', 'betray', 'launch', 'juiced', 'beyond', 'roster', 'trophy', 'shaped', 'humbug', 'motive', 'medley', 'spider', 'cooler', 'thinks', 'stewed', 'disown', 'eulogy', 'puller', 'repaid', 'usable', 'romper', 'snotty', 'matter', 'damsel', 'jazzed', 'tipper', 'mortal', 'bicker', 'intake', 'unable', 'former', 'wounds', 'barged', 'lifted', 'bowels', 'filmed', 'status', 'sequel', 'leeway', 'rehash', 'decker', 'choose', 'create', 'cement', 'yellow']

display = ""
word = ""
guess = ""
continued = False
used = []

play = True
while play == True:
	if not continued:
	    print(split)
	    print("Welcome to Wordle MK2 by Sean!")
	    print(split)
	    print("Please select your word length using the numbers on the left:\n")
	    print("1 | 4 Letters.")
	    print("2 | 5 Letters.")
	    print("3 | 6 Letters.")
	    print("4 | Custom Word.\n")
	    print(split)
	try:
		choice = int(input())
	except ValueError:
		print("Numbers only!\n")
		continued = True
		continue
	if choice == 1:
		word = random.choice(four)
		total = 4
	elif choice == 2:
		word = random.choice(five)
		total = 5
	elif choice == 3:
		word = random.choice(six)
		total = 6
	elif choice == 4:
		total = int(input("How long is the word? "))
		word = input(f"Please enter a word of {total} letters. (Make sure to hide the screen if you're choosing the word for someone) ")
		print("\n" * 20)
		print("\n" * 20)
		print("\n" * 10)
	else:
		print("That's not an option.")
		print(split)
		continued = True
		continue

	guesses = 0
	while guesses < 5:
		display = ""
		used = []
		guess = input(f"Please guess the word: ")
		if len(guess) != total or guess.isspace() or guess.isnumeric():
			print(f"Sorry, that's not a {total} letter word. Try again.")
			continue
		for index, letter in enumerate(guess):
				if letter in used and word.count(letter) == 1:
					display = colour.write(letter, black)
				elif letter == word[index]:
					display = colour.write(letter, green)
					used.append(letter)
				elif letter in word and letter != word[index]:
					display = colour.write(letter, orange)
					used.append(letter)
				else:
					display = colour.write(letter, black)
		guesses = guesses + 1
		print()
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
time.sleep(5.0)
