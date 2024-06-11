class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_arr = [0]*1001
        res = [0]*len(arr1)
        end = []
        arr2_set = set(arr2)
        pt = 0
        for i in arr1:
            if i not in arr2_set:
                end.append(i)
            count_arr[i] += 1
        
        for i in arr2:
            for j in range(count_arr[i]):
                res[pt] = i
                pt += 1
        pt2 = len(res) - 1
        end.sort()
        for i in range(len(end)-1, -1, -1):
            res[pt2] = end[i]
            pt2  -= 1
        return res
