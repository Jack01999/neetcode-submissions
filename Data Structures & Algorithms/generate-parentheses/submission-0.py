class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def isValid(paren: str) -> bool:
            stack = []
            for i in range(len(paren)):
                curr = paren[i]
                if curr == '(':
                    stack.append(curr)
                else:
                    if len(stack) > 0 and stack[len(stack)-1] == '(':
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
            


        def dfs(paren: str):
            if len(paren) >= n*2:
                if isValid(paren):
                    res.append(paren)
                return
            # Left - Yes
            dfs(paren + '(')
            # Right - No (backtrack)
            dfs(paren + ')')

        dfs("")
        return res
