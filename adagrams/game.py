# comment to practice push to GitHub
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
POINTS = {
    1:["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2:["D","G"],
    3:["B","C","M","P"],
    4:["F","H","V","W","Y"],
    5:["K"],
    8:["J","X"],
    10:["Q","Z"]
    }

def draw_letters():
    total_letter_pool = []
    hand = []

    # create a list with the total amount of letters: 
    for letter, quantity in LETTER_POOL.items():
        total_letter_pool.extend([letter for i in range(quantity)])
    
    # draw 10 random letters from list of letters and append it to the hand
    for i in range(10):
        random_index = randint(0,len(total_letter_pool)-1)
        random_letter = total_letter_pool.pop(random_index)
        hand.append(random_letter)
    return hand

def uses_available_letters(word, letter_bank):
    input_word = word.upper()
    copy_letter_bank = letter_bank.copy()

    # Check if each letter in the word exists in the letter bank
    for char in input_word: 
        if not char in copy_letter_bank:
            return False
        copy_letter_bank.remove(char)
    return True

def score_word(word):
    total_score = 0
    input_word = word.upper()

    # Iterate through score values and corresponding letters
    for score, letter_score in POINTS.items():
        for char in input_word:
            if char in letter_score:
                total_score += score
    
    # Bonus points for words with 7 or more letters
    if len(input_word) >= 7:
        total_score += 8
    return total_score

def get_highest_word_score(word_list):
    # Variables to track the highest score 
    winner_word = ""
    winner_score = 0

    # For loop to iterate over list of words
    for current_word in word_list:
        # Calculate and store score in a variable 
        current_score = score_word(current_word)

        # Update winner if current score is higher than the one storaged
        if current_score > winner_score:
            winner_word = current_word
            winner_score = current_score
        
        # Decide winner when a score tie happens
        elif current_score == winner_score:
            current_length = len(current_word)
            winner_length = len(winner_word)

            if current_length == 10 and winner_length != 10:
                winner_word = current_word
                winner_score = current_score
            elif current_length < winner_length and winner_length != 10:
                winner_word = current_word
                winner_score = current_score
        
        winner = (winner_word, winner_score)
    return winner