from random import randint
import random
from collections import Counter
from typing import Optional

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

# applied dict(sorted(LETTERS_SCORE.items())) to previous unsorted dictionary
LETTERS_SCORE = [
    {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 
    'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
]


def helper_letters_list(LETTER_POOL):
    # buils a list of letters according to their amount in LETTER_POOL
    letters_list = []
    for key, value in LETTER_POOL.items():
        for i in range(LETTER_POOL[key]):
            letters_list.append(key)

    return letters_list

letters_list = helper_letters_list(LETTER_POOL)


def draw_letters():
    tiles = []

    while len(tiles) < 10:
        random_integer = randint(0, len(letters_list)-1)
        letter = letters_list[random_integer]
        if tiles.count(letter) < LETTER_POOL[letter] and len(tiles) <10:
            tiles.append(letter)
        else:
            continue

    return tiles  

def uses_available_letters(word, letter_bank):

    for letter in word:
        if letter.upper() not in letter_bank:
            return False
        elif word.count(letter.upper()) > letter_bank.count(letter):
            return False
        
    return True


def score_word(word):
    score = 0
    word = word.upper()

    for letter in word:
        score += LETTERS_SCORE[letter]
    score += 8 if len(word) >= 7 else 0

    return score

def get_highest_word_score(word_list, debug_print = False):
    if not word_list:
        return None
    
    best_word = word_list[0]
    best_score = score_word(word_list[0])

    for i in range(1, len(word_list)):
        word = word_list[i]
        score = score_word(word)

        if debug_print:
            print(f'Checking {word}, score {score}')

        if score > best_score:
            best_score = score
            best_word = word
        elif score == best_score:
            if len(word) < len(best_word) and len(best_word) < 10 or\
            len(word) == 10 and len(best_word) < 10:
                best_word = word
                best_score = score

    return [best_word, best_score]
        
