class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # as we get a value we do not need the smaller values that are to the left
        # of it, and when this item is out of window we should remove it
        # we always keep the queue in monotonic decreasing order so the max will 
        # always be at dq[0] and if if out of range pop it
        res = []
        dq = deque()
        for i, n in enumerate(nums):
            while dq and nums[dq[-1]] <= n:
                dq.pop() # pop from the right
            dq.append(i) # we are sure now it is smaller than the left of it

            if dq[0] == i - k:  # out of range
                dq.popleft()
            if i >= k-1:
                res.append(nums[dq[0]])  # max one available
        return res
