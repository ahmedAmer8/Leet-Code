class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        current = 1
        while current <= 10**9:
            if Counter(str(n)) == Counter(str(current)):
                return True
            current *= 2
        
        return False
