class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bag = set() # Our special "No-Duplicates" box
        left = 0
        max_length = 0
        
        # 'right' is our hand picking up new candies
        for right in range(len(s)):
            # If the candy is already in the bag...
            while s[right] in bag:
                # ...throw away the candy on the far left
                bag.remove(s[left])
                left = left + 1
            
            # Now we can add the new candy
            bag.add(s[right])
            
            # How big is the bag now? (right - left + 1)
            current_bag_size = (right - left) + 1
            if current_bag_size > max_length:
                max_length = current_bag_size
                
        return max_length
