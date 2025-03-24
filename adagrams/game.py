from random import randint

def draw_letters():
    # Create a dictionary to track available letters
    letter_pool = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 
        'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 
        'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }
    
    # list of all letters
    all_letters = []
    for letter, count in letter_pool.items():
        all_letters.extend([letter] * count)
    
    # Draw 10 random letters from list
    hand = []
    remaining_letters = all_letters.copy() 
    
    for i in range(10):
        if remaining_letters:
            draw_position = randint(0, len(remaining_letters) - 1)
            selected_letter = remaining_letters.pop(draw_position)
            hand.append(selected_letter)
    
    return hand


def uses_available_letters(word, letter_bank):
    # Convert word to uppercase
    word = word.upper()
    
    # Increcrement count of letters or start count
    available_letters = {}
    for letter in letter_bank:
        if letter in available_letters:
            available_letters[letter] += 1
        else:
            available_letters[letter] = 1
    
    # Check if we have this letter or have used them all
    for letter in word:
        if letter not in available_letters or available_letters[letter] == 0:
            return False
        
        # Reduce avalibility count 
        available_letters[letter] -= 1
    
    # Get through whole word without running out of letters for word to be vaild
    return True

def score_word(word):

    # Convert word to uppercase
    word = word.upper()

    # Handle empty word case
    if not word:
        return 0
    
    # Mapp letters to point value
    point_values = {
        1: "A, E, I, O, U, L, N, R, S, T",
        2: "D, G",
        3: "B, C, M, P",
        4: "F, H, V, W, Y",
        5: "K",
        8: "J, X",
        10: "Q, Z"
    }
    
    letter_points = {}
    for points, letters in point_values.items():
        for letter in letters:
            letter_points[letter] = points
    
    # Calculate score by sum of points
    score = 0
    for letter in word:
        score += letter_points[letter]
    
    # Add bonus points for words 7-10 letters long
    if 7 <= len(word) <= 10:
        score += 8
    
    return score

def get_highest_word_score(word_list):

    if not word_list:
        return None
    
    word_positions = {}
    for i in range(len(word_list)):
        word = word_list[i]
        if word not in word_positions:
            word_positions[word] = i
    
    # Dctionary that stores each words metadata
    word_metadata = {}
    for word in word_list:
        word_metadata[word] = {
            'score': score_word(word),
            'length': len(word),
            'position': word_positions[word]
        }
    
    # Find the highest score
    highest_score = 0
    for word, metadata in word_metadata.items():
        if metadata['score'] > highest_score:
            highest_score = metadata['score']
    
    # Only show words with the highest score
    highest_words = []
    for word in word_list: 
        if word in word_metadata and word_metadata[word]['score'] == highest_score:
            highest_words.append(word)
            
    # Remove duplicates while preserving order
    highest_words = list(dict.fromkeys(highest_words))
    
    # If only one word has the highest score, return it
    if len(highest_words) == 1:
        winning_word = highest_words[0]
        return (winning_word, word_metadata[winning_word]['score'])
    
    # Tiebreaker 1 - Check for 10-letter words
    ten_letter_words = []
    for word in highest_words:
        if word_metadata[word]['length'] == 10:
            ten_letter_words.append(word)
    
    # If any word has exactly 10 letters, return the first one from the original list
    if ten_letter_words:
        best_word = ten_letter_words[0]
        for word in ten_letter_words:
            if word_metadata[word]['position'] < word_metadata[best_word]['position']:
                best_word = word
        
        return (best_word, word_metadata[best_word]['score'])
    
    # Tiebreaker 2 - Find shortest word length
    min_length = word_metadata[highest_words[0]]['length']
    for word in highest_words[1:]:  # Skip the first word since we already used it
        if word_metadata[word]['length'] < min_length:
            min_length = word_metadata[word]['length']
    
    shortest_words = []
    for word in highest_words:
        if word_metadata[word]['length'] == min_length:
            shortest_words.append(word)
    
    # If there's only one shortest word, return it
    if len(shortest_words) == 1:
        winning_word = shortest_words[0]
        return (winning_word, word_metadata[winning_word]['score'])
    
    # Tiebreaker 3 - If still tied, give preference to the first word in the original list
    best_word = shortest_words[0]
    for word in shortest_words:
        if word_metadata[word]['position'] < word_metadata[best_word]['position']:
            best_word = word
    
    return (best_word, word_metadata[best_word]['score'])

