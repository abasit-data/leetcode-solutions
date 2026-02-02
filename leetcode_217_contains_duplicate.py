class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        refrence = set(nums)
        if len(refrence) == len(nums):
            return False 
        return True
