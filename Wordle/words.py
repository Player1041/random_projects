import random, string
with open('popular.txt') as f:
    lines = f.readlines()

words = []
word_length = 6
number_of_words = 100

while len(words) < number_of_words:
    choice = random.choice(lines)
    if len(choice.strip('\n')) == word_length:
        words.append(choice.strip('\n').lower().strip(string.punctuation))

print(words)
