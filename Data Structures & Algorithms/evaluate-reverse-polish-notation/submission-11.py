class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        create a stack to hold the two integers before the operand
        when an operand, apply it to the two integers in the stack and then pop them from the stack
        add the result to the stack, becasue there will always be at least one more integer before the next operand
        """

        stack = []

        operators = {"+", "-", "*", "/"} #use a set because searching is faster

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                val1, val2 = stack.pop(), stack.pop() #since val1 is the first to be removed from the stack, its the rightmost
                stack.append(val2 - val1)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 // val1)
            else:
                stack.append(int(i))
        return stack[-1]