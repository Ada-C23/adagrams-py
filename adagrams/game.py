from random import randint

letter_pool = [
    'A'] * 9 + ['B'] * 2 + ['C'] * 2 + ['D'] * 4 + ['E'] * 12 + ['F'] * 2 + ['G'] * 3 + ['H'] * 2 + \
    ['I'] * 9 + ['J'] * 1 + ['K'] * 1 + ['L'] * 4 + ['M'] * 2 + ['N'] * 6 + ['O'] * 8 + ['P'] * 2 + \
    ['Q'] * 1 + ['R'] * 6 + ['S'] * 4 + ['T'] * 6 + ['U'] * 4 + ['V'] * 2 + ['W'] * 2 + ['X'] * 1 + \
    ['Y'] * 2 + ['Z'] * 1

def draw_letters():
    letter_bank = []
    available_letters = {}
    for letter in letter_pool:
        if letter in available_letters:
            available_letters[letter] += 1
        else:
            available_letters[letter] = 1
    
    while len(letter_bank) < 10:
        random_letter_index = randint(0, len(letter_pool) - 1)
        letter = letter_pool[random_letter_index]

        if available_letters[letter] > 0:
            letter_bank.append(letter)
            available_letters[letter] -= 1

    return letter_bank

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank = [letter.upper() for letter in letter_bank]

    letter_bank_dict = {}
    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] += 1
        else:
            letter_bank_dict[letter] = 1


    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for letter in letter_count:
        if letter not in letter_bank_dict:
            return False
        elif letter_count[letter] > letter_bank_dict[letter]: 
            return False
    return True
    

def score_word(word):
    word = word.upper()
    total_points = 0
    
    letter_scores = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
        'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
        }
    
    for letter in word:
        if letter in letter_scores:
            total_points += letter_scores[letter]
        
    if len(word) >= 7:
        total_points += 8

    return total_points

def get_highest_word_score(word_list):
    highest_score = 0
    best_word = ""
    
    for word in word_list:
        score = score_word(word)

        if score > highest_score:
            best_word = word
            highest_score = score
        
        elif score == highest_score:
            if len(word) == 10 and len(best_word) != 10:
                best_word = word
            
            elif len(best_word) == 10:
                continue

            elif len(word) < len(best_word):
                best_word = word
            
    return (best_word, highest_score)