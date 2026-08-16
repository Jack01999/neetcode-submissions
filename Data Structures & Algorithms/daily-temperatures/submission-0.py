class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)
        stack = [] # 2d array [temp, index]
        stack.append([temperatures[0], 0])
        for i in range(1, len(temperatures)):
            temp = temperatures[i]
            if temp <= stack[-1][0]:
                stack.append([temp, i])
            else:
                while len(stack) > 0 and temp > stack[-1][0]:
                    diff = i - stack[-1][1]
                    solution[stack[-1][1]] = diff
                    stack.pop()
                stack.append([temp, i])

        return solution
            
        