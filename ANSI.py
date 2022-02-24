print("\u001b[30;1m A \u001b[31;1m B \u001b[32;1m C \u001b[33;1m D \u001b[0m")

print("\u001b[43m\u001b[37;1mWhite with yellow background\u001b[0m")


fore_white = "\u001b[37;1m"
fore_black = "\u001b[40m"
back_black =  "\u001b[40m"
back_yellow = "\u001b[43m"
back_green = "\u001b[42m"
back_white =  "\u001b[47m"
reset = "\u001b[0m"

word = "feast"
guess = "featj"
display = ""



for index, letter in enumerate(guess):
    if letter == word[index]:
        display += f"{fore_black}{back_green}{letter}{reset}"
    elif letter in word and letter != word[index]:
        display += f"{fore_black}{back_yellow}{letter}{reset}"
    else:
        display += f"{fore_white}{back_black}{letter}{reset}"

print(display)
