class Solution:
    """
    we can't just use a delimeter with .join and .split because what if the delimeter is in one of the strings
    instead, we need to take the length of each string so we know how many characters to read before going to the next string
    separate the length of each string and the string itself with a special character (i.e. "#") and combine all strings into one to encode
    to decode, we read the length of the string, then append from the first pointer to the end of the string to the answer, repeat until the first pointer exceeds or equals length of string
    """



    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res # 3#dog3#cat5#mouse5#horse


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): #do not use for loop because we iterate i based on the value of j
            j = i #start where i is each time
            while s[j] != "#":
                j += 1 #iterate j until number is passed
            length = int(s[i: j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
            
