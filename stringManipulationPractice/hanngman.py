# Hangman game
# make a hangman game
# 2/5/26
# Thomas Stout

# taking word input and chaging it into *
word = input("Input a word ")

word_ast = []
for i in word:
    word_ast.append("*")

# guess = input("Please guess a letter : ").lower()

used_letters = []

# guesses left
wrong_guesses = 10
# num of word guesses left
word_guesses = 3

while True:
    guess = input(
        "Please guess a letter or your guees of the word (Only when your sure! You will only have 3 word guesses): "
    ).lower()
    # check if guess is just letter guess or word guess
    if len(guess) > 1:
        if guess == word:
            print(f"Correct! The word was {word}.")
        else:
            word_guesses -= 1
            print("You guessed the wrong word")
    else:
        # check if guess has already been made
        if guess in used_letters:
            continue
        # loops through word and finds where guess and letter matches then appends index of letter to n
        if guess in word:
            n = []
            for i in range(len(word)):
                if word[i] == guess:
                    n.append(i)
            for num in n:
                word_ast[num] = guess
            # add letter to list of used letters
            used_letters.append(guess)
        # if guess is wrong take away a wrong guess and add letter to list of used letters
        else:
            wrong_guesses -= 1
            used_letters.append(guess)
            if wrong_guesses == 0:
                print("You ran out of wrong guesses. You lost.")
                break
        print(used_letters)
        print(" ".join(word_ast))
        print(f"Wrong guesses remaining {wrong_guesses}.")
