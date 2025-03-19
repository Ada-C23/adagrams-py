from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters(): 
    # Create expanded list of letters based on frequency
    letter_bank = []
    for letter, frequency in LETTER_POOL.items():
        for _ in range(frequency):
            letter_bank.append(letter)
    
    # Draw 10 random letters
    letters = [] # changed variable from drawn_letters to letters
    for _ in range(10):
        index = randint(0, len(letter_bank) - 1) # get a random index
        letters.append(letter_bank.pop(index)) # append the letter
    
    print(f"Drawn letters: {letters}") # check output
    return letters        

def uses_available_letters(word, letters):
    # Convert letters in word to uppercase:
    word = word.upper()

    for letter in word: 
        if word.count(letter) > letters.count(letter):
            return False
    return True 
        

def score_word(word):
    word_total_score = 0

    letter_group_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    letter_group_2 = ["D", "G"]
    letter_group_3 = ["B", "C", "M", "P"]
    letter_group_4 = ["F", "H", "V", "W", "Y"]
    letter_group_5 = ["K"]
    letter_group_8 = ["J", "X"]
    letter_group_10 = ["Q", "Z"]

    # Convert word to uppercase to handle lowercase
    word = word.upper()

    for letter in word:
        if letter in letter_group_1:
            word_total_score += 1
        elif letter in letter_group_2:
            word_total_score += 2
        elif letter in letter_group_3:
            word_total_score += 3
        elif letter in letter_group_4:
            word_total_score += 4
        elif letter in letter_group_5:
            word_total_score += 5
        elif letter in letter_group_8:
            word_total_score += 8
        elif letter in letter_group_10:
            word_total_score += 10

    # Add bonus points for word length of 7-10 letters
    if len(word) >= 7 and len(word) <= 10: 
        word_total_score += 8

    return word_total_score


def get_highest_word_score(word_list):
    # Initialize variables to track the highest score and winning word
    highest_score = 0
    winning_word = None 

    # Loop through the list of words to get each word's score
    for word in word_list:
        score = score_word(word) # Use existing function to calculate score
        # If current word score is higher that existing highest_score, update highest score and winning word
        if score > highest_score:
            highest_score = score
            winning_word = word
        # If score of the current word is the same as the highest score apply rules
        elif score == highest_score:
            # the 10-letter word wins
            if len(word) == 10 and len(winning_word) != 10:
                winning_word = word
            # the word with the fewest letters wins
            elif len(word) < len(winning_word) and len(winning_word) != 10:
                winning_word = word
    
    winning_word_score = (winning_word, highest_score)
    
    # Return the winning word and its score
    return winning_word_score