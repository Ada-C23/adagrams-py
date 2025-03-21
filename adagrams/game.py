from random import randint

def draw_letters():
    #returns an array of ten strings each containing one letter
    #randomly drawn letters from pool of letters for the correct amount of letters available 
    #this function should **not** change the pool of letters

    LETTER_BANK_COUNT = {
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
    letter_pool = []
    for letter, count in LETTER_BANK_COUNT.items(): 
        for _ in range(count):
            letter_pool.append(letter)
    
    remaining_letters = {letter: count for letter, count in LETTER_BANK_COUNT.items()}
    
    player_tiles = []
    for _ in range(10):
        while True:
            index = randint(0, len(letter_pool)-1)
            letter = letter_pool[index]
        
            if remaining_letters[letter] > 0:
                player_tiles.append(letter_pool[index])
                remaining_letters[letter] -= 1
                break

    return player_tiles

print(draw_letters())

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_counts = {}
    for letter in letter_bank:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    for letter in word: 
        if letter in letter_counts and letter_counts[letter] > 0:
            letter_counts[letter] -= 1
        else:
            return False
    
    return True 

def score_word(word):
    score_word_points = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
}

    total_score = 0
    for letter in word:
        upper_letter = letter.upper()
        if upper_letter in score_word_points:
            total_score += score_word_points[upper_letter]
        
    if 7 <= len(word) <= 10:
        total_score += 8
    
    return total_score        

def get_highest_word_score(word_list):
    highest_word = word_list[0]
    highest_score = score_word(highest_word)
    
    for i in range(1, len(word_list)):
        word = word_list[i]
        score = score_word(word)
        
        if score > highest_score:
            highest_word = word
            highest_score = score
        elif score == highest_score:
            if len(highest_word) != 10:
                if len(word) == 10 or len(word) < len(highest_word):
                    highest_word = word
                    highest_score = score
    
    return (highest_word, highest_score)