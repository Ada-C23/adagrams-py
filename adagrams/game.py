from random import randint

def draw_letters():
    letters_list = []
    pool_of_letters_dict = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
        }

    pool_of_letters_array = []
    for key, value in pool_of_letters_dict.items():
        pool_of_letters_array += list(key) * value

    i = 0
    while len(letters_list) < 10:
        current_letter_pulled_index = randint(0, len(pool_of_letters_array)-1)
        letters_list.append(pool_of_letters_array[current_letter_pulled_index])
        pool_of_letters_array.pop(current_letter_pulled_index)
        i += 1

    return letters_list

def uses_available_letters(word, letter_bank):

    if not word.isalpha():
        return False
    word = word.upper()

    word_array = list(word)
    letter_bank_dict = {}

    for letter in letter_bank:
        letter_bank_dict[letter] = letter_bank_dict.get(letter, 0) + 1
        
    for letter in word:
        if letter_bank_dict.get(letter, 0) >= 1:
            letter_bank_dict[letter] = letter_bank_dict.get(letter, 0) - 1
        else:
            return False
    return True

def score_word(word):
    score = 0
    score_chart = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    if not word.isalpha():
        return False
    word = word.upper()
    
    for letter in word:
        score += score_chart[letter]

    if len(word) > 6:
        score += 8
    return score


def get_highest_word_score(word_list): 
    highest_score = 0
    h_score_data = ""
    
    for current_word in word_list:
        current_score = score_word(current_word)
        if (highest_score < current_score):
            highest_score = current_score
            h_score_data = current_word

        elif highest_score == current_score:
            if len(h_score_data) != 10 and len(current_word) != 10 and len(h_score_data) > len(current_word):
                highest_score = current_score
                h_score_data = current_word

            elif len(h_score_data) != 10 and len(current_word) == 10:
                highest_score = current_score
                h_score_data = current_word

    return h_score_data,highest_score
