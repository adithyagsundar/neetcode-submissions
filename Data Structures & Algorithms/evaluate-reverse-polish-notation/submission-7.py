class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        create a stack to hold the two integers before the operand
        when an operand, apply it to the two integers in the stack and then pop them from the stack
        add the result to the stack, becasue there will always be at least one more integer before the next operand
        """

        stack = []

        operators = ["+", "-", "*", "/"]

        for i in tokens:
            if i in operators:
                res = 0
                val1 = stack.pop()
                val2 = stack.pop()
                if i == "+":
                    res = val2 + val1
                elif i == "-":
                    res = val2 - val1
                elif i == "*":
                    res = val2 * val1
                elif i == "/":
                    res = val2 / val1
                stack.append(int(res)) #adding result to the stack
            else:
                stack.append(int(i))
        return stack[-1]