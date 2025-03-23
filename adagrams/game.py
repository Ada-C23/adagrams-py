from random import randint 

def create_letter_pool():
    letter_pool = []
    letter_pool.extend(["A"] * 9)
    letter_pool.extend(["B"] * 2)
    letter_pool.extend(["C"] * 2)
    letter_pool.extend(["D"] * 4)
    letter_pool.extend(["E"] * 12)
    letter_pool.extend(["F"] * 2)
    letter_pool.extend(["G"] * 3)
    letter_pool.extend(["H"] * 2)
    letter_pool.extend(["I"] * 9)
    letter_pool.extend(["J"] * 1)
    letter_pool.extend(["K"] * 1)
    letter_pool.extend(["L"] * 4)
    letter_pool.extend(["M"] * 2)
    letter_pool.extend(["N"] * 6)
    letter_pool.extend(["O"] * 8)
    letter_pool.extend(["P"] * 2)
    letter_pool.extend(["Q"] * 1)
    letter_pool.extend(["R"] * 6)
    letter_pool.extend(["S"] * 4)
    letter_pool.extend(["T"] * 6)
    letter_pool.extend(["U"] * 4)
    letter_pool.extend(["V"] * 2)
    letter_pool.extend(["W"] * 2)
    letter_pool.extend(["X"] * 1)
    letter_pool.extend(["Y"] * 2)
    letter_pool.extend(["Z"] * 1)
    return letter_pool


def draw_letters():
    #Create the data structure containing the letters and letter distribution.
    letter_pool = create_letter_pool()

    #Randomly select 10 characters from the data structure
    letter_hand = []
    for i in range(10):
        #Generates a random integer between 0 and the last element in letter_pool list.
        random_index = randint(0,len(letter_pool)-1)
        #Access an element within letter_pool list, determined by random_index.
        random_letter = letter_pool[random_index]
        #Add the newly generated random letter to letter_hand list.
        letter_hand.append(random_letter)
        #Remove the random_letter from letter_pool
        letter_pool.remove(random_letter)

    #Return letter_hand list of 10 letters.
    return letter_hand


def uses_available_letters(word, letter_bank):
    word = word.upper()
    #Create a dictionary for word to store the word and its frequency.
    word_count = {}
    #Iterate through each element in word and add it to word_count dictionary.
    for char in word:
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
    

    #Create a dictionary for letter_bank to store each word and its frequency.
    letter_bank_count = {}
    #Iterate through each element in letter_bank list and add it to letter_bank_count dictionary.
    for i in letter_bank:
        if i in letter_bank_count:
            letter_bank_count[i] += 1
        else:
            letter_bank_count[i] = 1

    
    #For every letter in word_count, the letter in letter_bank_count is greater than or equal to it.
    #Iterate through word_count dictionary
    for char in word_count.keys():
        if char not in letter_bank_count or word_count[char] > letter_bank_count[char]:
            return False
    return True
        


def score_word(word):
    word = word.upper()
    #Create a dictionary to store score chart.
    letter_values = {
        'A': 1,
        'B': 3,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 2,
        'H': 4,
        'I': 1,
        'J': 8,
        'K': 5,
        'L': 1,
        'M': 3,
        'N': 1,
        'O': 1,
        'P': 3,
        'Q': 10,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 1,
        'V': 4,
        'W': 4,
        'X': 8,
        'Y': 4,
        'Z': 10
    }
    word_score = 0


    #Iterate through word string
    for char in word:
    #Match each char in word to element in letter_values
        letter_value = letter_values[char]
        #Sum the value of element(value) of letter_values and store in word_score
        word_score += letter_value
        #If the length of word is 7,8,9,10 - add 8 to word_score
    if len(word) == 7 or len(word) == 8 or len(word) == 9 or len(word) == 10:
        word_score += 8
    return word_score



def get_highest_word_score(word_list):
    best_score = 0
    best_scoring_tuple = None
    #Iterate through every word in word_list.
    for word in word_list:
        #Get the score of each word.
        word_score = score_word(word)
        #Add word and it's score to tuple
        word_score_tuple = (word, word_score)


        #Check if the current word's score is greater than best_score variable
        if word_score > best_score:
            #Update best_score variable to equal word_score
            best_score = word_score
            #Update best_scoring_tuple to that word's tuple.
            best_scoring_tuple =  word_score_tuple
        #Check if word_score is the same as best_score
        elif word_score == best_score:
            best_word = best_scoring_tuple[0]
            #Count the letters in word and check if they're equal to 10
            if len(word) == 10 and len(best_word) != 10:
                best_scoring_tuple = word_score_tuple
            elif len(best_word) > len(word) and len(best_word) != 10:
                best_scoring_tuple = word_score_tuple


    return best_scoring_tuple



