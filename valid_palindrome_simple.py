class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_text = ""
        for character in s:
            if character.isalnum(): # Is it a letter or number?
                cleaned_text += character.lower()
        
        
        left = 0
        right = len(cleaned_text) - 1
        
        while left < right:
            
            if cleaned_text[left] != cleaned_text[right]:
                return False
            
            
            left = left + 1
            right = right - 1
            
       
        return True
