from random import randint

"""input:no parameters 
output: returns an array(list) of ten strings
each string should contain exactly one letter """
#edge cases
#letters should be randomly drawn from a pool of letters
#  

LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

#WAVE 1
def draw_letters():
    """Draws letters from the letter pool randomly and returns a new list without the drawn letter"""
    # Step 1: create a list 
    letter_list = []
    #for loop goes through each letter in letterpool and counts the frequency of thst letter
    for letter, count in LETTER_POOL.items():
        #creates a list of that letter repeated and adds copies to letter_list
        letter_list.extend([letter] * count)  
    
    # Step 2: Draw 10 random letters
    #create empty list to store letters that are drawn
    drawn_letters = []
    # loop 10 times to draw 10 letters
    for _ in range(10):
        #pick a random index to draw from 
        random_index = randint(0, len(letter_list) - 1) 
        #removes that letter from the pool of letters 
        drawn_letters.append(letter_list.pop(random_index))  
    return drawn_letters


#WAVE2
def uses_available_letters(word, letter_bank):
    word = word.upper()  # Convert the word to uppercase to match letter_bank format
    letter_counts = {}  #Create dictionary to count how many times each letter appears in the bank

    #Go through each letter in letter_bank and count how many times each appears
    for letter in letter_bank:
        if letter in letter_counts:
            letter_counts[letter] += 1  #Add to the existing count if the letter is already in the dictionary
        else:
            letter_counts[letter] = 1  #Start a new count if the letter hasn't been seen yet

    # Check if each letter in the word is in the letter bank and not overused
    for letter in word:
        if letter in letter_counts and letter_counts[letter] > 0:
            letter_counts[letter] -= 1  # Use one occurrence of the letter
        else:
            return False  #Letter is either not in the bank or used too many times

    return True  #All letters in the word are valid and available in the bank

#WAVE3
def score_word(word):
    #Convert the word to uppercase to match the score chart letters
    word = word.upper()

    # Create groups of letters that are worth the same points
    one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    two_points = ['D', 'G']
    three_points = ['B', 'C', 'M', 'P']
    four_points = ['F', 'H', 'V', 'W', 'Y']
    five_points = ['K']
    eight_points = ['J', 'X']
    ten_points = ['Q', 'Z']

    # Start score at 0
    score = 0

    # Go through each letter in the word and check which group it belongs to
    for letter in word:
        if letter in one_point:
            score += 1
        elif letter in two_points:
            score += 2
        elif letter in three_points:
            score += 3
        elif letter in four_points:
            score += 4
        elif letter in five_points:
            score += 5
        elif letter in eight_points:
            score += 8
        elif letter in ten_points:
            score += 10

    # Add 8 bonus points if the word is 7 to 10 letters long
    if len(word) >= 7 and len(word) <= 10:
        score += 8

    return score

#WAVE4
def get_highest_word_score(word_list):
    # Set starting score and best word placeholders
    highest_score = 0
    best_word = ""

    #Loop through each word in the word_list
    for word in word_list:
        score = score_word(word)  #Get the score of the current word

        #If the word has a higher score, update the best word and score
        if score > highest_score:
            highest_score = score
            best_word = word

        # If the score is the same as the highest, use tie-breaking rules
        elif score == highest_score:
            # Rule 1: Prefer the word with fewer letters (shortest word)
            if len(word) < len(best_word) and len(best_word) != 10:
                best_word = word
            # Rule 2: Unless one word has exactly 10 letters, prefer the 10-letter word
            elif len(word) == 10 and len(best_word) != 10:
                best_word = word
            # Rule 3: If same length and score, keep the first one (already handled by order of loop)

    #Return the best word and its score as a tuple
    return (best_word, highest_score)