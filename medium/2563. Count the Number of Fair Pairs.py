def bin_search(target, l, r):
            while l <= r:
                m = l + (r-l)//2
                if nums[m] < target:
                    l = m +1
                else:
                    r = m -1
            return r

        nums.sort()
        n = len(nums)
        pairs = 0
        for i in range(n):
            cur = nums[i]
            l = bin_search(lower - cur, i+1, n-1)
            r = bin_search(upper - cur + 1, i+1, n-1)
            pairs += r - l
        return pairs
