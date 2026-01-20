"""
Problem: Find the Index of the First Occurrence in a String (strStr)

Given two strings:
- haystack (the main string)
- needle (the substring to find)

Task:
Return the index of the first occurrence of needle in haystack.
If needle does not exist, return -1.

Example:
haystack = "sadbutsad"
needle = "sad"
Output: 0

Approach:
- Slide over the haystack string
- At each index, take a substring of the same length as needle
- Compare it with needle
- If matched, return the index

Time Complexity: O(n × m)
Space Complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: empty needle
        if needle == "":
            return 0

        # Loop through possible starting positions
        for i in range(len(haystack) - len(needle) + 1):
            # Check substring match
            if haystack[i:i + len(needle)] == needle:
                return i

        # If needle not found
        return -1
