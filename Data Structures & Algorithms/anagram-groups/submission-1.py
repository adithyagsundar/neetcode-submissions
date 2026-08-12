class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """

        if frequency maps are the same, then two strings are anagrams
        create a frequency map for each string in strs
        freq_list : ["act", "cat"]
        freq_list: ["stop", "pots", "tops"]
        ...

        """

        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 #unique index value for each of 26 chars
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())

        

