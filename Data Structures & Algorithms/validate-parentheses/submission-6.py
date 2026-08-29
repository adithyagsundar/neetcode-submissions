class Solution:
    def isValid(self, s: str) -> bool:
        """
        the last opening parenthesis will be the top of the stack since its the first one to be closed
        we use a hashmap to map closing to opening
        if they match and the last element of the stack is the opening, then we pop from the stack
        if the stack is empty at the end, we return true

        """
        stack = []
        pairs = {"]": "[", "}" : "{", ")" : "("}

        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0