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

LETTER_VALUES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

HAND_SIZE = 10

def draw_letters():
    """
    build a hand of 10 letters for the user
    Parameters:    None
    Returns:
    a list of strings with single letters
    """     
    #step1: create a pile of letter based on letter pool
    letter_list = []
    for letter, count in LETTER_POOL.items():
        while count > 0:            
            letter_list.append(letter)
            count -= 1
    #step2:randomly pick 10 letters from the letter_pool: for each pick, update count, remove letter from letter_list if count gets to 0;  
    hand = []

    while len(hand) < HAND_SIZE:
        n = len(letter_list)
        index = randint(0, n - 1)
        letter = letter_list[index]
        hand.append(letter)
        #swap letter at index with last index
        letter_list[index], letter_list[n-1] = letter_list[n-1], letter_list[index]
        letter_list.pop()
    return hand

def uses_available_letters(word, letter_bank):
    """
    Check if an input word from a user only used characters that are within the hand list
    Parameters:
    - word as a string
    - letter_bank as a list of drawn letters in a hand
    Return: boolean
    """
    # create letter_freq_dict for letters in letter_bank
    letter_freq_dict = {}
    for letter in letter_bank:
        letter_freq_dict[letter] = letter_freq_dict.get(letter, 0) + 1
    # iterate through each character in word string and check if char exists and compare counts; update counts when finding a matching
    for char in word.upper():
        if not char in letter_freq_dict or letter_freq_dict[char] == 0:
            return False
        else:
            letter_freq_dict[char] -= 1
    return True

def score_word(word):
    """
    Score the word from user input
    Parameters: word as a string of chars
    output: int (number of points)    
    """
    # create LETTER_VALUES as a global variable outside (see top)
    # iterate through word string, find points for each char and add them up, check length for extra points
    score = 0
    for char in word.upper():
        score += LETTER_VALUES[char]
    if len(word) in [7, 8, 9, 10]:
        score += 8
    return score

def get_highest_word_score(word_list):
    """
    Find word with highest score
    Parameter: a list of strings
    Output: a tuple with a string and the score    
    """
    # calculate score for each word and store in word_scores dict, also update highest score
    word_scores = {}
    highest_score = 0
    for word in word_list:
        score = score_word(word)
        word_scores[word] = score
        if score > highest_score:
            highest_score = score
    # loop through the word_list, find all words with highest score
    words_with_highest_score = []
    for word in word_list:
        if word_scores[word] == highest_score:
            words_with_highest_score.append(word)
    
    winning_word = words_with_highest_score[0]
    # return if no ties
    if len(words_with_highest_score) == 1:
        return winning_word, highest_score
    # find the shortest word, also check if length of 10 exists    
    smallest_length = len(winning_word)
    for word in words_with_highest_score:
        if len(word) == 10:
            return (word, highest_score)
        if len(word) < smallest_length:
            winning_word = word
            smallest_length = len(word)
    return winning_word, highest_score
