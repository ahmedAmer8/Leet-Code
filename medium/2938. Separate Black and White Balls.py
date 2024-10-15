class Solution:
    def minimumSteps(self, s: str) -> int:
        # start from the end, each 1 needs to be swapped with all zeros to its
        # right, so we just count the number of zeros to the right and each time
        # we meet 1 we add zero count to the res
        zeros = 0
        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                zeros += 1
            else:
                res += zeros
        return res
