from random import randint 

# define letter pool
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}
# define score chart
SCORE_CHART = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 
    2: ['D', 'G'], 
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'], 
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

# make letter pool of all potential letters
def get_all_letters():
    full_letter_list = []
    for letter, frequency in LETTER_POOL.items():
        full_letter_list += [letter] * frequency
    return full_letter_list

# generate 10 random letters using random index of full letter list 
def draw_letters():
    full_letter_list = get_all_letters()
    hand = []
    for i in range(10):
        if not full_letter_list: # check if list is empty
            break
        index = randint(0, len(full_letter_list) -1)
        hand.append(full_letter_list.pop(index)) # return and remove chosen letter to adhere to frequency count for next loop
    return hand      


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:] # make copy to modify without altering original hand
    for char in word.upper(): # removes case sensitivity
        if char in letter_bank_copy:
            letter_bank_copy.remove(char) # remove used letter from hand to ensure no repetitions
        else:
            return False
    return True

def score_word(word):

    score = 0
    if 7 <= len(word) <= 10: # adds 8 extra points to words with 7-10 letters
        score += 8

    for char in word.upper():
        for points, letters in SCORE_CHART.items(): # find character in letter values and match it to key (point)
            if char in letters:
                score += points
    return score


def get_highest_word_score(word_list):

    top_score = 0    
    top_word = ""

    for word in word_list:
        word_score = score_word(word)

        if word_score > top_score:
            top_score = word_score
            top_word = word # replaces top score and top word as it loops through the word_list
        elif word_score == top_score:
            if len(top_word) == 10 or len(word) == len(top_word):
                continue # does not replace top word if the previous word already has 10 letters and is same length
            elif len(word) == 10 and len(top_word) != 10:
                top_word = word # first word with 10 letters wins
            elif len(word) < len(top_word):
                top_word = word # prefer the shorter word with same score
    
    return (top_word, top_score)
    
    