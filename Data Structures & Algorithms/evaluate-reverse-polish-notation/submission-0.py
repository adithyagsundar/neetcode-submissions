class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ["+", "-", "*", "/"]

        for i in tokens:
            if i in operators:
                second = stack.pop()
                if i == "+":
                    val = stack[-1] + second
                elif i == "-":
                    val = stack[-1] - second
                elif i == "*":
                    val = stack[-1] * second
                elif i == "/":
                    val = stack[-1] / second
                stack.pop()
                stack.append(val)
            else:
                stack.append(i)
        return stack[-1]

            