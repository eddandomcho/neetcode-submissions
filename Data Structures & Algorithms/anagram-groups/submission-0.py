class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        current_index = 0
        big_dict = dict()
        final_list = list()
        for word in strs:
            if "".join(sorted(word)) not in big_dict:
                big_dict["".join(sorted(word))] = [word]
                continue
            big_dict["".join(sorted(word))].append(word)
        return list(big_dict.values())
