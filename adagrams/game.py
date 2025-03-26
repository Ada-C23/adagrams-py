from random import randint
HAND_SIZE = 10
BONUS_MIN_LENGTH = 7
LENGTH_BONUS_POINTS = 8

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

SCORE_OF_LETTER = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}


def draw_letters():
    letters = []
    available_pool = []
    #To reflect the real possibility, we need to update the dictionary to list of letters
    #In this way each letter in the pool will have same possibility to be selected by randint
    for letter, counts in LETTER_POOL.items():
        for count in range(counts):
            available_pool. append(letter)
    while len(letters) < HAND_SIZE:
        random_index = randint(0, len(available_pool) - 1)
        letters.append(available_pool.pop(random_index))  #update the pool
    
    return letters



def uses_available_letters(word, letter_bank):
    status = False
    count_of_letter_mapping = {}

    for letter in letter_bank:
        if letter in count_of_letter_mapping:
            count_of_letter_mapping[letter]+= 1
        else:
            count_of_letter_mapping[letter]= 1

    for letter in word:
        if letter.upper() in letter_bank and count_of_letter_mapping[letter.upper()]>0:
            count_of_letter_mapping[letter.upper()] -= 1
            status = True
        else:
            status = False
            return status  #add a return statement so that we return False immediately when seeing invalid letter
    return status


def score_word(word):
    score = 0
    for letter in word:
        score += SCORE_OF_LETTER[letter.upper()]
    if len(word) >= BONUS_MIN_LENGTH:
        score += LENGTH_BONUS_POINTS
    return score

def get_highest_word_score(word_list):
    highest_score = 0
    winner = ""
    for word in word_list:
        score_of_word = score_word(word)
        if score_of_word > highest_score:
            highest_score = score_of_word
            winner = word
        #Updated tie condition
        elif score_of_word == highest_score:
            if len(winner) != 10 and len(word) == 10:  #First check if the given word has 10 letters since it's preferable under tie condition
                winner = word                              #Also check if the winner word already has 10 letters so that when multiple words having same length same score, we pick the first word.
            elif len(winner) != 10 and len(word) < len(winner):  #If the given word doesn't have 10 letters, check if this word has fewer letters. 
                winner = word                                        #Also need to check if the winner has 10 letters because we don't want to acdientally update the winner to word that has fewer letter (again, 10 letters is the most perferable under tie condition)

    return winner,highest_score
    