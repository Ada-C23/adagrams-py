from random import randint

LETTERS_DICT = {
    "A": 9, "B": 2, "C": 2, "D": 4,
    "E": 12, "F": 2, "G": 3, "H": 2,
    "I": 9, "J": 1, "K": 1, "L": 4,
    "M": 2, "N": 6, "O": 8, "P": 2,
    "Q": 1, "R": 6, "S": 4, "T": 6,
    "U": 4, "V": 2, "W": 2, "X": 1,
    "Y": 2, "Z": 1
}

LETTERS_SCORE = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1,
    "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}


def draw_letters():
    hand = []
    letters_list = []

    for letter, count in LETTERS_DICT.items():
        letters_list.extend(letter * count)
    
    for i in range(10):
        random_letter_index = randint(0, len(letters_list) - 1)
        letter = letters_list.pop(random_letter_index)
        hand.append(letter)
    return hand

def uses_available_letters(word, letter_bank):
    word_upper = word.upper()
    bank_dict = {}

    for letter in letter_bank: 
        bank_dict[letter] = bank_dict.get(letter, 0) + 1

    for letter in word_upper:
        if letter not in bank_dict or bank_dict[letter] == 0:
            return False
        
        bank_dict[letter] -= 1

    return True

def score_word(word):
    word_upper = word.upper()
    score = 0

    for letter in word_upper:
        score += LETTERS_SCORE[letter]

    if len(word) > 6:
        score += 8

    return score

def get_highest_word_score(word_list):
    best_score = ["", 0]

    for word in word_list:
        word_score = score_word(word)

        if word_score > best_score[1]:
            best_score[0] = word
            best_score[1] = word_score

        elif word_score == best_score[1] and len(best_score[0]) != 10:
            if len(word) == 10 or len(word) < len(best_score[0]):
                best_score[0] = word
                best_score[1] = word_score

    return tuple(best_score)
