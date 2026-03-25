key_word = input("Enter a word for hangman: ").lower()
star_word = "*" * len(key_word)

wrong_guesses = int(input("How many guesses do you want: "))

while wrong_guesses > 0:
    guess = input("Guess a letter: ").lower()
    working_word = ""

    for i in range(len(key_word)):
        if key_word[i] == guess:
            working_word += guess
        else:
            working_word += star_word[i]

    if guess not in key_word:
        wrong_guesses -= 1
        print(f"Wrong! You have {wrong_guesses} left!")
        
    star_word = working_word
    print(f"Here is what you have so far: {star_word}")

    if star_word == key_word:
        print("You gussed all of the letters within the word.")
        break
