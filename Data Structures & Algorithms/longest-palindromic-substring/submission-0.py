class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ""
        def count_from_center(left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1
            return s[left + 1: right]
        for i in range(0, len(s)):
            # Fix 2: Check both odd-length (single center) and even-length (double center) palindromes
            odd_p = count_from_center(i, i)
            even_p = count_from_center(i, i + 1)
            
            # Keep track of the maximum length palindrome found
            if len(odd_p) > len(longest):
                longest = odd_p
            if len(even_p) > len(longest):
                longest = even_p
        return longest