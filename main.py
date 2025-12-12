import random

myDict = {
    "A" : """
        __     
       /  \\   
      /____\\  
     /      \\ 
    /        \\""",
    "a" : """
        __     
       /  \\    
      /____\\   
     /      \\  
    /        \\ """,
    "B" : """
    |¯¯¯\\
    |   /
    |--- 
    |   \\
    |___/""",
    "b" : """
    |¯¯¯\\
    |   /
    |--- 
    |   \\
    |___/""",
    "c" : """
     ____
    |    
    |    
    |    
     ¯¯¯¯
    """,
    "C" :"""
     ____
    |    
    | 
    |    
     ¯¯¯¯
    """,
    "d" : """
    |¯¯¯\\
    |    |
    |    |
    |    |
    |___/""",
    "D" :"""
    |¯¯¯\\
    |    |
    |    |
    |    |
    |___/""",
    "e" :"""
     ___
    |   
    |___
    |   
     ¯¯¯""",
    "E" :"""
     ___
    |   
    |___
    |   
     ¯¯¯""",
    "f" :"""
    ____
    |   
    |___
    |   
    |   """,
    "F" : """
    ____
    |   
    |___
    |   
    |   """,
    "g" : """
     ___ 
    |    
    |  _ 
    |   |
    |___|""",
    "G" : """
     ___ 
    |    
    |  _ 
    |   |
    |___|""",
    "h" : """
    |   |
    |   |
    |---|
    |   |
    |   |""",
    "H" : """
    |   |
    |   |
    |---|
    |   |
    |   |""",
    "i" : """
    _____
      |  
      |  
      |  
    ¯¯¯¯¯""",
    "I" : """
    _____
      |  
      |  
      |  
    ‾‾‾¯¯""",
    "k" : """
    |  /
    | / 
    |-  
    | \\ 
    |  \\""",
    "K" : """
    |  /
    | / 
    |-  
    | \\ 
    |  \\""",
    "j" : """
    _____
      |  
      |  
      |  
    \\_/  """,
    "J" : """
    _____
      |  
      |  
      |  
    \\_/  """,
    "l" : """
    |    
    |    
    |    
    |    
    |____""",
    "L" : """
    |    
    |    
    |    
    |    
    |_____""",
    "m" : """
    |\\   /|
    | \\ / |
    |  v  |
    |     |
    |     |""",
    "M" : """
    |\\   /|
    | \\ / |
    |  v  |
    |     |
    |     |""",
    "n" : """
    |\\    |
    | \\   |
    |  \\  |
    |   \\ |
    |    \\|""",
    "N" : """
    |\\    |
    | \\   |
    |  \\  |
    |   \\ |
    |    \\|""",
    "o" : """
     ___ 
    |   |
    |   |
    |   |
     ‾‾‾ """,
    "O" : """
     ___ 
    |   |
    |   |
    |   |
     ‾‾‾ """,
    "p" : """
    |¯¯¯\\ 
    |    |
    |___/ 
    |     
    |     """,
    "P" : """
    |¯¯¯\\ 
    |    |
    |___/ 
    |     
    |     """,
    "q" : """
     ___ 
    |   |
    |   |
    |  \\|
     ¯¯¯ """,
    "Q" :"""
     ___ 
    |   |
    |   |
    |  \\|
     ¯¯¯ """,
    "r" :"""
    |¯¯¯\\ 
    |    |
    |___/ 
    |   \\ 
    |    \\""",
    "R" : """
    |¯¯¯\\ 
    |    |
    |___/ 
    |   \\ 
    |    \\""",
    "s" : """
     ____
    |    
    |____
        |
    ____|""",
    "S" : """
     ____ 
    |     
    |____ 
        |
    ____|""",
    "t" : """
    _____
      |  
      |  
      |  
      |  """,
    "T" : """
    _____
      |  
      |  
      |  
      |  """,
    "u" : """
    |   |
    |   |
    |   |
    |   |
    |___|""",
    "U" : """
    |   |
    |   |
    |   |
    |   |
    |___|""",
    "v" : """
    |    |
    |    |
    \\    /
     \\  / 
      \\/  """,
    "V" : """
    |    |
    |    |
    \\    /
     \\  / 
      \\/  """,
    "w" : """
    |   |
    | | |
    | | |
    | | |
    \\/ \\/""",
    "W" : """
    |   |
    | | |
    | | |
    | | |
    \\/ \\/""",
    "x" : """
    \\   /
     \\ / 
      x  
     / \\ 
    /   \\""",
    "X" : """
    \\   /
     \\ / 
      x  
     / \\ 
    /   \\""",
    "y" : """
    \\   /
     \\ / 
      v  
      |  
      |  """,
    "Y" : """
    \\   /
     \\ / 
      v  
      |  
      |  """,
    "z" : """
    _____
        /
       / 
      /  
     /   
    /____""",
    "Z" : """
    _____
        /
       / 
      /  
     /   
    /____""",
    "_" : """
         
         
         
         
    _____""",
    " " : """
         
         
         
         
         """,
    "0" : """
     ### 
    #   #
    #   #
    #   #
     ### """,
    "1" : """
      #  
     ##  
      #  
      #  
     ### """,
    "2" : """
     ### 
    #   #
      ## 
     #   
    #####""",
    "3" : """
     ### 
    #   #
      ## 
    #   #
     ### """,
    "4" : """
    #  # 
    #  # 
    #####
       # 
       # """,
    "5" : """
    #####
    # 
    ####
        #
    #### """,
    "6" : """
     ### 
    #    
    #### 
    #   #
     ### """,
    "7" : """
    #####
       # 
      #  
     #   
     #   """,
    "8" : """
     ### 
    #   #
     ### 
    #   #
     ### """,
    "9" : """
     ### 
    #   #
     ####
        #
     ### """,
    "'" : """
      #  
      #  
     #   
         
         """
}

def hangman(lives):
    if lives == 6:
        print("""
        |-/-----------|
        |/            |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |""")
    elif lives == 5:
        print("""
        |-/-----------|
        |/            |
        |            ___
        |           /   \\
        |          | 0 0 |
        |          |  _  |
        |           \\___/
        |            
        |
        |
        |
        |
        |
        |
        |
        |
        |""")
    elif lives == 4:
        print("""
        |-/-----------|
        |/            |
        |            ___
        |           /   \\
        |          | 0 0 |
        |          |  _  |
        |           \\___/
        |             |
        |             |
        |             |
        |             |
        |             |
        |
        |
        |
        |
        |""")
    elif lives == 3:
        print("""
        |-/-----------|
        |/            |
        |            ___
        |           /   \\
        |          | 0 0 |
        |          |  _  |
        |           \\___/
        |             |
        |            /|
        |           / | 
        |          /  |  
        |             |
        |
        |
        |
        |
        |""")
    elif lives == 2:
        print("""
        |-/-----------|
        |/            |
        |            ___
        |           /   \\
        |          | 0 0 |
        |          |  _  |
        |           \\___/
        |             |
        |            /|\\
        |           / | \\
        |          /  |  \\
        |             |
        |
        |
        |
        |
        |""")
    elif lives == 1:
        print("""
        |-/-----------|
        |/            |
        |            ___
        |           /   \\
        |          | 0 0 |
        |          |  _  |
        |           \\___/
        |             |
        |            /|\\
        |           / | \\
        |          /  |  \\
        |             |
        |            /
        |           /
        |          /
        |
        |""")
    elif lives == 0:
        print("""
        |-/-----------|
        |/            |
        |            ___
        |           /   \\
        |          | 0 0 |
        |          | ⏞ |
        |           \\___/
        |             |
        |            /|\\
        |           / | \\
        |          /  |  \\
        |             |
        |            / \\
        |           /   \\
        |          /     \\
        |
        |         YOU LOSE
        |""")

def main():
    lives = 6
    word = getWord().lower()
    wordGuessed = ""
    wordLength = len(word) 
    guess = ""
    firstCheck = 0
    lettersGuessed = []
    wordsGuessed = []
    if wordGuessed == "":
        wordGuessed = "_" * wordLength
    for i in (range(len(word))):
        if word[i] == " ":
            wordGuessed = wordGuessed[:i] + " " + wordGuessed[i+1:]
        if word[i] == "'":
            wordGuessed = wordGuessed[:i] + "'" + wordGuessed[i+1:]
    while wordGuessed != word:
        validity = 0
        print("\n")
        for part in wordGuessed.split():      
            for row in range(6):              
                for letter in part:
                    print(myDict[letter].splitlines()[row], end=" ")
                print()                       
            print()  
        print("\n")
        hangman(lives)
        if firstCheck >0:
            print(f"Letters Guessed: {sorted(lettersGuessed)}")
            print(f"Words Guessed: {sorted(wordsGuessed)}")
        else: firstCheck += 1
        guess = input("What is your next guess? (Please enter a single letter, number, or a word(s) the same length as the hidden word(s))")
        if guess in lettersGuessed:
            print(f"You have already guessed {guess}. Try again!")
        elif guess in wordsGuessed:
            print(f"You have already guessed {guess}. Try again!")
        else:
            if len(guess) == 1:
                for i in range(len(word)):
                    if word[i] == guess.lower():
                        wordGuessed = wordGuessed[:i] + guess + wordGuessed[i+1:]
                        validity = 1
                lettersGuessed.append(guess)
                if validity == 0:
                    lives -= 1
            elif len(guess) == len(word):
                wordsGuessed.append(guess.lower())
                if guess.lower() == word.lower():
                    wordGuessed = guess
                else: lives -= 1
            else: print(f"Your guess of {guess} is invalid. Try again!")
            if lives == 0:
                hangman(0)
                print(f"The word was {word}. Better luck next time!")
                break
            if wordGuessed == word:
                for part in wordGuessed.split():      
                    for row in range(6):              
                        for letter in part:
                            print(myDict[letter].splitlines()[row], end=" ")
                        print()                       
                    print()  
                hangman(lives)
                print("                   YOU WIN!\n")

def getWord():
    with open("cubingInput.txt", "r") as wordList:
        content = wordList.read()
        words = [w.strip() for w in content.split(",")]
        return random.choice(words)

if __name__ == "__main__":
    main()

