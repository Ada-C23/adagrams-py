import random 
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
#creat a list with all letters in right amount show
    letter_pool = []
    for letter, times in LETTER_POOL.items():   
        for i in range(times):
            letter_pool.append(letter)
#creat a list with user's random letter
    letter_bank = []
    while len(letter_bank) < 10:
        draw = random.randint(0, len(letter_pool)-1)
        user_letter = letter_pool[draw]
        letter_bank.append(user_letter)
        letter_pool.remove(user_letter)  
    return letter_bank
    

def uses_available_letters(word, letter_bank):
    word_list = list(word.lower())
    letter_bank = [letter.lower() for letter in letter_bank]
    letter_bank_new = letter_bank
    correct_list = []
    for i in word_list:
        if i in letter_bank:
            correct_list.append(i)
            letter_bank_new.remove(i)
        else:
            return False
    return correct_list == word_list


def score_word(word):
    letter_values = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}
    word = list(word.upper())
    score = 0
    if len(word) > 6:
        score += 8
    for i in word:
        score += letter_values[i]
    return score


def get_highest_word_score(word_list):
    #creat a score_list, contains tuples as ("word", score)
    score_list = []
    for word in word_list:
        word_tuple = (word, score_word(word))
        score_list.append(word_tuple)
    # print(score_list)

    #tie-rule: 1. shortest len(word) win; 2. len(word) > 10 wins; 
    # 3. lower index[word_list] win   
    highest_score = 0
    winner_word = score_list[0][0]
    for word, score in score_list:
        if score > highest_score:
            highest_score = score  
            winner_word = word
        elif score == highest_score:
            if len(word) >= 10 and len(winner_word) < 10:
                winner_word = word
                # print("short win", winner_word)
            elif len(word) < 10 and len(word) < len(winner_word) and len(winner_word) < 10:
                winner_word = word  
                # print("ten win", winner_word)
            elif word_list.index(word) < word_list.index(winner_word):
                winner_word = word
                # print("early win", winner_word)
    return (winner_word, highest_score)
    

