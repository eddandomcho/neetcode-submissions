class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        state = dict()
        ans = 0
        for right in range(len(s)):
            state[s[right]] = state.get(s[right], 0) + 1
            while state[s[right]] > 1:
                state[s[left]] -= 1
                if state[s[left]] == 0:
                    del state[s[left]]
                left += 1  # Contract left edge
            ans = max(ans, right - left + 1)
        return ans