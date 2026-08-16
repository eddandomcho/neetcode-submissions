class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        state = set()
        ans = 0
        for right in range(len(s)):
            while s[right] in state:
                state.remove(s[left])
                left +=1
                # moving left until the duplicate instance of s[right] is wiped out.
            state.add(s[right])
            ans = max(ans, right - left + 1)
        return ans