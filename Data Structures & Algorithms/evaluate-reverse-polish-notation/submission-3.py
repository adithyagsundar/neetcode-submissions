class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ["+", "-", "*", "/"]

        for i in tokens:
            if i in operators:
                res = 0
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if i == "+":
                    res = val1 + val2
                elif i == "-":
                    res = val1 - val2
                elif i == "*":
                    res = val1 * val2
                elif i == "/":
                    res = val1 / val2
                stack.append(res)
            else:
                stack.append(i)
        return stack[-1]