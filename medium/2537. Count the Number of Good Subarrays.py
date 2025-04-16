class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        n = len(nums)
        left = 0
        right = 0
        res = 0
        freq = defaultdict(int)
        pairs = 0

        while left < n:
            while right < n and pairs < k:
                freq[nums[right]] += 1
                if freq[nums[right]] >= 2:
                    pairs += freq[nums[right]] - 1
                right += 1
            
            if pairs >= k:
                res += n - right + 1

            freq[nums[left]] -= 1
            if freq[nums[left]] > 0:
                pairs -= freq[nums[left]]
            left += 1
        
        return res
