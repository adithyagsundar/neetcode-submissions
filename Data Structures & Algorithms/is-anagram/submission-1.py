class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        sorted strings must be the same
        """

        return sorted(s) == sorted(t)