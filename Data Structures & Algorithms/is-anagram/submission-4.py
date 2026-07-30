class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        create a hashmap, store each letter in both the strings to a key value pair in the hashmap
        if each letters frequency value is 2, then then return True
        """

        hashmap = {}

        for letter in s + t:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
        
        for key, value in hashmap.items():
            if value % 2 != 0:
                return False
        return True
        
        
