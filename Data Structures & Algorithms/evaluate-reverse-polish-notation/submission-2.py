class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            # print(stack)
            if tokens[i] == "+":
                calc = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(calc)
            elif tokens[i] == "*":
                calc = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(calc)
            elif tokens[i] == "-":
                calc = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(calc)
            elif tokens[i] == "/":
                calc = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(calc)
            else:
                stack.append(tokens[i])


        return int(stack[0])
        