class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        strs = [dog, cat, mouse, horse]

        3#dog, 3#cat, 5#mouse, 5#horse
        """

        res = ""

        for s in strs:
            res = str(len(s)) + "#" + s 
        return res #3dog3#cat5#mouse5#horse
        


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #pointer that updates when each string is done

        while i < len(s):
            j = 0
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i += j + 1 + length
        return res 
