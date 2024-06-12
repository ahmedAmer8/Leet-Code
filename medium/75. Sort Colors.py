class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(f, s):
            a[f], a[s] = a[s], a[f]
        ptr = 0
        l, r = 0, len(a) - 1
        while ptr <= r:
            if a[ptr] == 2:
                swap(ptr, r)
                r -= 1
                ptr -= 1
            elif a[ptr] == 0:
                swap(ptr, l)
                l += 1
            ptr += 1
