class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        for i in range(len(s)):
            curr = s[i]
            if curr == '(' or curr == '[' or curr == '{':
                stack.append(curr)
            elif curr == ')':
                if len(stack) > 0 and stack[len(stack)-1] == '(':
                    stack.pop()
                else:
                    return False
            elif curr == ']':
                if len(stack) > 0 and stack[len(stack)-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                if len(stack) > 0 and stack[len(stack)-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        