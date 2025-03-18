from random import randint

def draw_letters():
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
    letter_bank = []
    letter_pool_list = []
    for letter in LETTER_POOL:
        letter_pool_list.extend([letter] * LETTER_POOL[letter])
    
    for i in range(10):
        letter_index = randint(0, len(letter_pool_list)-1)
        letter_bank.append(letter_pool_list.pop(letter_index))
    return letter_bank
        

def uses_available_letters(word, letter_bank):
    letter_list = letter_bank[:]
    for letter in word:
        if letter.upper() not in letter_list:
            return False
        else:
            letter_list.remove(letter.upper())
    return True


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
    scores = 0
    for letter in word:
        scores+=letter_values[letter.upper()]
    if len(word)>=7 and len(word)<=10:
        scores+=8
    return scores


def get_highest_word_score(word_list):
    
    best_word = [0] *2
    for word in word_list:
        score = score_word(word)
        if score> best_word[1]:
            best_word[0] = word
            best_word[1] = score
        elif score == best_word[1]:
            if len(word) ==10 and len(best_word[0])!=10:
                best_word[0] = word
                best_word[1] = score
            elif len(best_word[0])!=10 and len(word) < len(best_word[0]):
                best_word[0] = word
                best_word[1] = score

    return best_word

