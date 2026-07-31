class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        if the length is not equal, return false
        create a hashmap for each string
        store frequency count of each character in string in hashmaps
        anagrams would have the exact same frequency of characters
        """
        
        if len(s) != len(t):
            return False #lengths not equal

        hashmapS, hashmapT = {}, {}

        for i in range(len(s)):
            hashmapS[s[i]] = hashmapS.get(s[i], 0) + 1 #increment by one for each count of the character, use .get for if the value doesn't already exist
            hashmapT[t[i]] = hashmapT.get(t[i], 0) + 1

        for char in hashmapS:
            if hashmapS[char] != hashmapT.get(char, 0):
                return False
        return True