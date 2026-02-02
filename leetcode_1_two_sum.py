class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        notebook = {} 
        
        for i, number in enumerate(nums):
            friend_we_need = target - number
            
            # --- THE SEARCH ---
            if friend_we_need in notebook:
                # We found the index of the friend in our notebook
                index_of_friend = notebook[friend_we_need]
                # Return both indices as a list
                return [index_of_friend, i]
            
            # --- THE STORAGE ---
            # If no friend found, store CURRENT number and its index
            # This allows future numbers in the loop to find THIS number
            notebook[number] = i
            
        return [] # Empty list if no pair exists
