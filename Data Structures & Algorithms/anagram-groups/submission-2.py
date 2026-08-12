class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """

        create a frequency list for each string in strs
        append strings to the value of a hashmap containing each freq_list as keys
        return the values of the hashmap

        freq_list : ["eat", "tea", "ate"]
        freq_list : ["nat", "tan"]
        ...

        """

        res = defaultdict(list) # if count doesn't already exist

        for s in strs:
            freq_map = [0] * 26 # freq of each character for each string, a ... z
            for c in s:
                freq_map[ord(c) - ord("a")] += 1 # a @ 0, b @ 1, c @ 2 ...
            res[tuple(freq_map)].append(s)
        return list(res.values())


                



