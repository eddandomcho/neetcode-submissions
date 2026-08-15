class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        # Sort the dictionary items by value in descending order and take the first k keys
        return sorted(freq, key=freq.get, reverse=True)[:k]