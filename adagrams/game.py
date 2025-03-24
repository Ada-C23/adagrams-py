from random import randint

def draw_letters():
    # Letter distribution as per the provided table
    LETTER_DISTRIBUTION = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1,
        'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2,
        'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }

    # Create a pool of letters based on their frequency
    LETTER_POOL = []
    for letter, count in LETTER_DISTRIBUTION.items():
        LETTER_POOL.extend([letter] * count)
    """Draws 10 random letters from the letter pool."""
    hand = []
    for _ in range(10):
        index = randint(0, len(LETTER_POOL) - 1)  # Random index within the pool
        hand.append(LETTER_POOL[index])  # Pick the letter at the random index
    return hand

def uses_available_letters(word, letter_bank):
    """Checks if the word can be formed using letters from the letter_bank."""
    word = word.upper()  # Convert to uppercase for case insensitivity
    letter_count = {}

    # Count occurrences of each letter in the letter_bank
    for letter in letter_bank:
        letter_count[letter] = letter_count.get(letter, 0) + 1
        # Check if the word can be formed with available letters
    for letter in word:
        if letter not in letter_count or letter_count[letter] == 0:
            return False  # Letter is missing or used too many times
        letter_count[letter] -= 1  # Use up one instance of the letter

    return True

def score_word(word):
    # Letter score table
    letter_scores = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    # Convert the word to uppercase for consistency
    word = word.upper()

    # Calculate the base score
    score = sum(letter_scores.get(letter, 0) for letter in word)
    
    # Add bonus if the word length is between 7 and 10
    if 7 <= len(word) <= 10:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    """Returns the word with the highest score, applying tie-breaking rules."""
    
    # Initialize variables to track the best word and its score
    best_word = ""
    best_score = 0
    best_length = float('inf')  # Start with a very large number
    best_is_ten = False  # Whether the best word has 10 letters
    # Iterate through each word in the word list
    for word in word_list:
        # Get the score for the current word
        current_score = score_word(word)
        current_length = len(word)
        current_is_ten = current_length == 10
    # Apply tie-breaking rules
        if current_score > best_score:
            # New highest score, update the best word and score
            best_word = word
            best_score = current_score
            best_length = current_length
            best_is_ten = current_is_ten
        elif current_score == best_score:
            if current_is_ten and not best_is_ten:
                # Prefer the word with 10 letters
                best_word = word
                best_score = current_score
                best_length = current_length
                best_is_ten = True
            elif current_length < best_length:
                # Prefer the word with fewer letters
                best_word = word
                best_score = current_score
                best_length = current_length
                best_is_ten = current_is_ten
    return (best_word, best_score)