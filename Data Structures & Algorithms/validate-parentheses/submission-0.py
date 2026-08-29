class Solution:
    def isValid(self, s: str) -> bool:
        """
        ][
        )]}{[(
        every opening bracket comes BEFORE a closing bracket
        if a closing bracket, check if the correspondign open bracket is at the TOP OF THE STACK. this is because we want to make sure that there are NO OTHER brackets in between
        """

        brackets = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                brackets.append(c)
                continue
            if c != brackets.pop(): #top of the stack
                return False
        return True
            



        
