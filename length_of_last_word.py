# ==========================================
# Title: Length of Last Word
# Concept: String Manipulation
# Logic: Strip the spaces, split into words, 
#        and measure the very last one.
# ==========================================

def length_of_last_word(s: str) -> int:
    # This is the "Pythonic" way (doing it all in one line!)
    # 1. strip() removes outer spaces
    # 2. split() breaks it into a list of words
    # 3. [-1] picks the last word
    # 4. len() counts the letters
    
    words = s.strip().split()
    
    if not words:
        return 0
        
    return len(words[-1])

# Testing the logic
if __name__ == "__main__":
    test_string = "   Fly me   to   the moon  "
    result = length_of_last_word(test_string)
    print(f"The length of the last word is: {result}") # Output: 4
