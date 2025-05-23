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
    letter_bank = ['A','A','A','A','A','A','A','A','A', 'B','B', 'C', 'C', 'D', 'D', 'E', 'E','E','E','E','E','E','E','E','E','E','E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I','I','I','I','I','I','I','I','J', 'K', 'L','L','L','L', 'M', 'M', 'N','N','N','N','N','N', 'O', 'O','O','O','O','O','O','O', 'P', 'P', 'Q', 'R','R','R','R','R','R', 'S', 'S','S','S', 'T', 'T', 'T','T','T','T', 'U','U','U','U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']
    available_letters = build_letters_and_availability_list(LETTER_POOL)
    # let pile = makePile() helper or list coomprehennsion to build based on letter distribution
    # const numTilesAllowedInHand = 10
    while len(letter_bank) < 10:
        # for loop in range 10
        index_of_letter = get_index_of_letter() # refactor - const getRandIndex() 

        if not available_letters[index_of_letter]['is_not_available']:
    
            letter_bank.append(available_letters[index_of_letter]['letter'])
            available_letters[index_of_letter]['is_not_available'] = True

    reset_available_letters(available_letters)

    return letter_bank

def build_letters_and_availability_list(letter_pool):
    available_letters = []
    
    for letter, letter_distribution in letter_pool.items():
        for single_letter in range(letter_distribution):
            available_letters.append({'letter':letter, 'is_not_available':False})
    
    return available_letters

def uses_available_letters(word, letter_bank):
    letters_in_word = list(word.upper())
    is_valid = False

    for letter in word:
        same_letter_count = letters_in_word.count(letter) <= letter_bank.count(letter)
        
        if word.count(letter) > 0 and same_letter_count:
            continue
        else:
            return is_valid
    
    is_valid = True

    return is_valid

def score_word(word):
    SCORE_CHART = {
        1 : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2 : ['D', 'G'],
        3 : ['B', 'C', 'M', 'P'],
        4 : ['F', 'H', 'V', 'W', 'Y' ],
        5 : ['K'],
        8 : ['J', 'X' ],
        10 : ['Q', 'Z']
    }
    BONUS_POINTS = 8
    score = 0
    word_case_insensitive = word.upper()

    for letter in word_case_insensitive:
        for points, letters in SCORE_CHART.items():
            if letter in letters:
                score += points

    if len(word) >= 7:
        score += BONUS_POINTS

    return score

def get_highest_word_score(word_list):
    words_and_scores = build_words_and_scores_dict(word_list)
    top_score = 0
    highest_scores = []
    winning_word_and_score = []

    for current_word, current_score in words_and_scores.items():
        if top_score == 0 or current_score == top_score:
            top_score = current_score
            highest_scores.append([current_word, current_score])
        elif current_score > top_score:
            top_score = current_score
            highest_scores[0] = [current_word, current_score]
    
    if len(highest_scores) > 1:
        winning_word_and_score = check_for_a_tie(highest_scores)
    else:
        winning_word_and_score = highest_scores[0]

    return tuple(winning_word_and_score)

def get_index_of_letter():
    return randint(0, 97)

def reset_available_letters(available_letters):
    for letter in range(len(available_letters)):
        available_letters[letter]['is_not_available'] = False

def build_words_and_scores_dict(word_list):
    words_with_scores_dict = {}

    for current_word in word_list:
        current_score = score_word(current_word)
        words_with_scores_dict[current_word] = current_score
    
    return words_with_scores_dict

def check_for_a_tie(words_and_scores):
    winning_word_and_score = []
    words_with_same_len = [] 
    
    for current_word_and_score in range(len(words_and_scores)):
        if not winning_word_and_score:
            winning_word_and_score = words_and_scores[current_word_and_score]
        if len(words_and_scores[current_word_and_score][0]) == 10:
            winning_word_and_score = words_and_scores[current_word_and_score]
            break
        elif len(words_and_scores[current_word_and_score][0]) == len(winning_word_and_score[0]):
            words_with_same_len.append(words_and_scores[current_word_and_score])
        elif len(words_and_scores[current_word_and_score][0]) < len(winning_word_and_score[0]):
            winning_word_and_score = words_and_scores[current_word_and_score]
 
    return winning_word_and_score

