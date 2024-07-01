class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        helper = 0
        for num in arr:
            if num % 2 == 1:
                helper += 1
                if helper == 3:
                    return True
            else:
                helper = 0
        return False