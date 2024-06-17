def merge_sort(nums, l, r):
    if l >= r:
        return
    m = l + (r-l)//2
    merge_sort(nums, l, m)
    merge_sort(nums, m+1, r)
    merge(nums, l, m, r)
def merge(nums, l, m, r):
    # number of elements in each array
    n1 = m-l+1
    n2 = r-m

    # extra space to hold the original elements as we will modify nums
    L = nums[l:m + 1]
    R = nums[m + 1:r + 1]

    i,j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]: nums[k] = L[i]; i += 1

        else: nums[k] = R[j]; j += 1
        
        k += 1

    while i < n1:
        nums[k] = L[i]
        k += 1
        i += 1
    while j < n2:
        nums[k] = R[j]
        k += 1
        j += 1

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge_sort(nums, 0, len(nums)-1)
        return nums
