class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        if the length of the strings are not the same, immediately return false
        create a hashmap for each string
        make each character in the string maps to a frequency value
        anagrams will have the exact same count and frequency of characters
        """

        if len(s) != len(t):
            return False
        
        hashmap_s, hashmap_t = {}, {}

        for i in range(s):
            hashmap_s[s[i]] += 1
            hashmap_t[t[i]] += 1
        return hashmap_s == hashmap_t

        

        
        
