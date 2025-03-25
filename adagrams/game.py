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

LETTERS_SCORE = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

LETTERS_LIST = [
    'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 
    'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I',
    'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 
    'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T',
    'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z'
]

def draw_letters():
    
    tiles = []
    for x in range(10):
        random_integer = random.randint(0, len(LETTERS_LIST)-1)
        letter = LETTERS_LIST[random_integer]
        if tiles.count(letter) == LETTER_POOL[letter]:
            break
        tiles.append(letter)
    return tiles  

def uses_available_letters(word, letter_bank):

    word = word.upper()
    word_counts = Counter(word)
    letter_bank_counts = Counter(letter_bank)
    
    for letter, count in word_counts.items():
        if letter_bank_counts[letter] < count:
            return False
    
    return True

def score_word(word):
    score = 0
    word = word.upper()

    for letter in word:
        score += LETTERS_SCORE[letter]
    score += 8 if len(word) >= 7 else 0

    return score

def get_highest_word_score(word_list):
    if not word_list:
        return None
    
    best_word = word_list[0]
    best_score = score_word(word_list[0])

    for i in range(1, len(word_list)):
        word = word_list[i]
        score = score_word(word)

        if score > best_score:
            best_score = score
            best_word = word
        elif score == best_score:
            if len(word) < len(best_word) and len(best_word) < 10 or\
            len(word) == 10 and len(best_word) < 10:
                best_word = word
                best_score = score

    return [best_word, best_score]
        