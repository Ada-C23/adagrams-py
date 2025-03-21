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

SCORE_CHART = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
}


def draw_letters():
    letter_pool_list = []

    for letter in LETTER_POOL:
        count = LETTER_POOL[letter]
        for copy in range(count):
            letter_pool_list.append(letter)

    letter_bank = []

    while len(letter_bank) < 10:
        random_index = randint(0, len(letter_pool_list) - 1)
        drawn_letter = letter_pool_list[random_index]
        letter_pool_list.remove(drawn_letter)
        letter_bank.append(drawn_letter)

    return letter_bank


def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_counts = {}

    uppercase_letter_bank = []
    for letter in letter_bank:
        uppercase_letter_bank.append(letter.upper())
    letter_bank = uppercase_letter_bank

    for letter in letter_bank:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
            
    for letter in word:
        if letter in letter_counts and letter_counts[letter] > 0:
            letter_counts[letter] -=1
        else:
            return False

    return True


def score_word(word):

    if word == "":
        return 0

    total_score = 0

    for letter in word:
        letter = letter.upper()
        if letter in SCORE_CHART:
            total_score += SCORE_CHART[letter]

    if len(word) >= 7:
        total_score += 8

    return total_score


def get_highest_word_score(word_list):

    best_word = word_list[0]
    best_score = score_word(word_list[0])

    for word in word_list:
        score = score_word(word)
        
        if score > best_score:
            best_word = word
            best_score = score
        
        elif score == best_score:
            if len(word) < len(best_word) and len(best_word) != 10:
                best_word = word
            elif len(word) == 10 and len(best_word) != 10:
                best_word = word

    return (best_word, best_score)