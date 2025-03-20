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
    letter_pool = LETTER_POOL.copy()
    letters_list = list(letter_pool.keys())
    draw_letters_list = []
    
    while len(draw_letters_list) < 10:
        letter_index = randint(0, len(letters_list) -1)
        letter = letters_list[letter_index]
        if letter_pool[letter] > 0:
            draw_letters_list.append(letter)
            letter_pool[letter] -= 1
    
    
    return draw_letters_list
    
#Comment added just to practice push it to GitHub
def uses_available_letters(word, letter_bank):
    available_letters = letter_bank[:]
    word = word.upper()
    for letter in word: 
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False
    return True

def score_word(word):
    letter_score = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 
        'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    word = word.upper()
    total_points = 0 
    for letter in word:
        total_points += letter_score[letter]
    if len(word) >=7:
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
                highest_score = score
                
            elif len(word) < len(best_word) and len(best_word) != 10:
                best_word = word
                highest_score = score

    return (best_word, highest_score)