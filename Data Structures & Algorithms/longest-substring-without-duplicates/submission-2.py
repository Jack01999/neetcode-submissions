class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge case (Len <= 1):
        if len(s) <= 1:
            return len(s)

        solution = 1
        left, right = 0, 1
        seenSet = set()
        seenSet.add(s[left])
        while right < len(s):
            if s[right] not in seenSet:
                seenSet.add(s[right])
                right += 1
                solution = max(solution, len(seenSet))
            else:
                while s[left] != s[right]:
                    seenSet.remove(s[left])
                    left += 1
                seenSet.remove(s[left])
                left += 1


        return solution

