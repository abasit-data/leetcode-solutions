# ==========================================
# Title: Plus One
# Concept: Array Iteration (Right-to-Left)
# Logic: Add 1 to the last digit. Carry over if 
#        the digit is a 9.
# ==========================================

def plus_one(digits):
    """
    Increments the integer represented by the list of digits by one.
    """
    n = len(digits)
    
    # Walk backwards
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        # If digit is 9, change to 0 and continue loop
        digits[i] = 0
    
    # If we are here, all digits were 9
    return [1] + digits

# Testing the logic
if __name__ == "__main__":
    print(f"Test [1,2,3]: {plus_one([1,2,3])}") # Output: [1,2,4]
    print(f"Test [4,3,2,9]: {plus_one([4,3,2,9])}") # Output: [4,3,3,0]
    print(f"Test [9,9]: {plus_one([9,9])}") # Output: [1,0,0]
