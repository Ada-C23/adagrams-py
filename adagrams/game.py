from random import randint

def draw_letters():
#create a list of letters
    letters = [
    'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
    'B', 'B', 
    'C', 'C', 
    'D', 'D', 'D', 'D', 
    'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 
    'F', 'F', 
    'G', 'G', 'G', 
    'H', 'H', 
    'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 
    'J', 
    'K', 
    'L', 'L', 'L', 'L', 
    'M', 'M', 
    'N', 'N', 'N', 'N', 'N', 'N', 
    'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 
    'P', 'P', 
    'Q', 
    'R', 'R', 'R', 'R', 'R', 'R', 
    'S', 'S', 'S', 'S', 
    'T', 'T', 'T', 'T', 'T', 'T', 
    'U', 'U', 'U', 'U', 
    'V', 'V', 
    'W', 'W', 
    'X', 
    'Y', 'Y', 
    'Z'
]
#choose 10 letters from the list above
#create an empty list 'hand'
    hand = []
#create 'for' loop to choose a letter from the list 'letters', randomly
#'append' adds the letter to the list 'hand'
#'pop' removes the appended letter from the list 'letters'
    for _ in range(10):
        random_index = randint(0,len(letters) - 1)
        hand.append(letters[random_index]) 
        letters.pop(random_index)

    return hand
    
#print(draw_letters())
#print(len(draw_letters()))

def uses_available_letters(word, letter_bank):
#create a copy of letter_bank to avoid changing the original list of letters
    letter_bank_copy = letter_bank[:]
#make each letter uppercase
    word = word.upper()
#create a loop to remove used letter from the list if a letter was in the word
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
        
    return True

#word = "HELLO"
#letter_bank = ["H", "E", "L", "L", "O", "A", "B", "C", "D", "E"]
#print(uses_available_letters(word, letter_bank))


def score_word(word):
#add all meanings for possible letters, dictionary
    score_chart = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}
#we want to know a score, every time a score starts with 0
    score = 0  
    word = word.upper()
#create 'for' loop to add meanings of letters to their score
    for letter in word:  
        score += score_chart.get(letter, 0)
#add bonus condition
    if len(word) >= 7:
        score += 8

    return score

#print(score_word("HELLO"))

def get_highest_word_score(word_list):
#tulip 'best_word', one arg str, another int
    best_word = ["", 0]  

#create 'for' loop to find the best score
    for word in word_list:
        score = score_word(word)

#the best word is a word with higher score
        if score > best_word[1]:
            best_word[0] = word
            best_word[1] = score
#if score is the same:
        elif score == best_word[1]:
#the winner is the word with 10 letters
            if len(word) == 10 and len(best_word[0]) != 10:
                best_word[0] = word
#if not, the winner is the smalllest word
            elif len(word) < len(best_word[0]) and len(best_word[0]) != 10:
                best_word[0] = word

    return tuple(best_word)

#words = ["HELLO", "SCIENCE", "COMPUTER", "DEVELOPER"]
#print(get_highest_word_score(words))
