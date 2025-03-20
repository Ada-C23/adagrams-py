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
    pile = []
    hand = []
    # created a list of letters
    for k, v in LETTER_POOL.items():  
        for counter in range(0, v):      
            pile.append(k)

    for i in range(10):
        index = randint(0, len(pile)-1)
        hand.append(pile[index])
        del pile[index]

    return hand

def uses_available_letters(word, letter_bank):
    word = word.upper()
    bank_copy = letter_bank.copy()
    for ch in word:
        if ch in bank_copy:
            bank_copy.remove(ch)
        else:
            return False
    return True

def score_word(word):
    total = 0
    score_chart = {
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10
    }
    for ch in word.upper():
        total += score_chart[ch]
    if len(word) > 6 and len(word) < 11:
        total += 8
    return total

def get_highest_word_score(word_list):
    highest_score = -1
    highest_word = ""

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            highest_word = word
        elif highest_score == score and len(word) == 10 and len(highest_word) != 10:
            highest_word = word
        elif highest_score == score and len(word) < len(highest_word) and len(highest_word) != 10:
            highest_word = word
    return (highest_word, highest_score)


