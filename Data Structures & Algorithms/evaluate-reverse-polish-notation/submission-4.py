class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ["+", "-", "*", "/"]

        for i in tokens:
            if i in operators:
                res = 0
                val1 = stack.pop()
                val2 = stack.pop()
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
                stack.append(int(i))
        return stack[-1]