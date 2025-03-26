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
    letters = []
    for key, value in LETTER_POOL.items():
        for _ in range(value):
            letters.append(key)
    hand = []
    for _ in range(10):
        index = randint(0, len(letters) - 1)
        letter = letters.pop(index)
        hand.append(letter)
    return hand

def uses_available_letters(word, letter_bank):
    letter_bank_counts = {}
    for letter in letter_bank:
        if letter in letter_bank_counts:
            letter_bank_counts[letter] += 1
        else:
            letter_bank_counts[letter] = 1

    for letter in word.upper():
        if letter in letter_bank_counts and letter_bank_counts[letter] > 0:
            letter_bank_counts[letter] -= 1
        else:
            return False

    return True

def score_word(word):
    score_chart = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}
    score = 0
    for letter in word.upper(): 
        score += score_chart[letter]
    if 7 <= len(word) <= 10:
        score += 8
    return score


def get_highest_word_score(word_list):
    top_score = 0
    best_words = []

    for word in word_list:
        score = score_word(word) 

        if score > top_score:
            top_score = score
            best_words = [word]  
        elif score == top_score:
            best_words.append(word)  

    if len(best_words) == 1:
        return (best_words[0], top_score)

    winning_word = best_words[0]  

    for word in best_words:
        if len(word) == 10:  
            return (word, top_score)
        if len(word) < len(winning_word):  
            winning_word = word

    return (winning_word, top_score)