"""
Problem: Remove Element

Given an array nums and a value val,
remove all occurrences of val in-place
and return the number of remaining elements.

Approach:
- Use two pointers
- Move valid elements forward
- Ignore elements equal to val

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
