class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # without extra space
        n = len(boxes)
        res = [0]*n

        leftOnes = 0 if boxes[0] == '0' else 1
        rightOnes = 0 if boxes[n-1] == '0' else 1
        leftShifts = rightShifts = 0

        for i in range(n-2, -1, -1):
            rightShifts += rightOnes
            rightOnes += 0 if boxes[i] == '0' else 1 
        
        # as we start at index 1
        if boxes[0] == '1': 
            rightOnes -= 1

        res[0] = rightShifts
        for i in range(1, n):
            # calculate left shifts
            leftShifts += leftOnes
            leftOnes += 0 if boxes[i] == '0' else 1

            # calculate current right shifts, all right ones go step back
            rightShifts -= rightOnes
            rightOnes -= 1 if boxes[i] == '1' else 0

            res[i] = leftShifts + rightShifts
        return res
