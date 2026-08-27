class Solution:
    def minWindow(self, s: str, t: str) -> str:
        solution = [-1,-1]
        solutionLen = float("infinity")
        countT, window = {}, {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        have, need = 0, len(countT)
        print(need)

        left, right = 0, 0
        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
            while have == need:
                currLen = right - left + 1
                if currLen < solutionLen:
                    solution = [left, right]
                    solutionLen = currLen

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
            right += 1
        print(solution)
        if solutionLen != float("infinity"):
            return s[solution[0] : solution[1] + 1]
        else:
            return ""