class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort first
        sortedList = [(p, s) for p,s in zip(position, speed)]
        sortedList.sort(reverse=True)

        stack = []
        for p, s in sortedList:
            calc = (target - p) / s
            stack.append(calc)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        