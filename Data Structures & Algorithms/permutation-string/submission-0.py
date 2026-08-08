class Solution:
    def isPermutation(self, s1: str, s2: str) -> bool:
        # Should be equal length
        s1Map = {}
        s2Map = {}
        for i in range(len(s1)):
            s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
            s2Map[s2[i]] = 1 + s2Map.get(s2[i], 0)
        #print(s1Map)
        #print(s2Map)

        return s1Map == s2Map
        

    def checkInclusion(self, s1: str, s2: str) -> bool:
        solution = True
        if len(s2) < len(s1):
            return False
        left, right = 0, len(s1)
        while right <= len(s2):
            window = s2[left:right]
            print(window)
            isPerm = self.isPermutation(s1, window)
            if isPerm == True:
                return True
            left += 1
            right += 1


        return False
        