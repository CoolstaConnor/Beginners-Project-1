s1 = "______"
s2 = """
   |
   |
   |
   |
___|___
"""
s3 = """
   ______
   |
   |
   |
   |
___|___
"""
s4 = """
 ______
   |/
   |
   |
   |
___|___ 
"""
s5 = """
  ______
   |/   |
   |
   |
   |
___|___ 
"""
s6 = """
  ______
   |/   |
   |    0
   |
   |
___|___
"""
s7 = """
   ______
   |/   |
   |    0
   |    |
   |
___|___
"""
s8 = """
 ______
   |/   |
   |    0
   |   <|
   |
___|___ 
"""
s9 = """
  ______
   |/   |
   |    0
   |   <|>
   |
___|___ 
"""
s10 = """
   ______
   |/   |
   |    0
   |   <|>
   |    /
___|___
"""
s11 = """
   ______
   |/   |   
   |    0
   |   <|>
   |   / \ 
___|___ 
"""

def hangmanprint(numguesses):
    stages = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
    if 0 <= numguesses < len(stages):
        print(stages[numguesses])

def correctword(word, correct_letters):
    display = []
    for letter in word:
        if letter in correct_letters:
            display.append(letter)
        else:
            display.append('_')
    print(' '.join(display))

def makeguesses(word):
    global numguesses
    wrongguesses = set()
    correct_letters = set()
    while numguesses < 11:
        letter = input("Guess a letter: ").lower()
        if letter in wrongguesses or letter in correct_letters:
            print(f"Letter {letter} has already been guessed.")
            continue
        if letter in word:
            print(f"{letter} is in the word.")
            correct_letters.add(letter)
        else:
            print(f"The letter {letter} is not included in the word.")
            wrongguesses.add(letter)
            numguesses += 1

        correctword(word, correct_letters)
        hangmanprint(numguesses)
        
        if set(word) <= correct_letters:
            print("Congratulations! You've guessed the word!")
            return True
        
        if numguesses >= 10:
            print(f"Game Over! The word was: {word}.")
            return False
numguesses = 0
word = "product"

# Start the game
if not makeguesses(word):
    correctword(word, set(word))