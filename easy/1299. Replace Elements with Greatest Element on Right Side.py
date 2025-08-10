class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_largest = -1
        res = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            res[i] = right_largest
            right_largest = max(arr[i], right_largest)
        
        return res
