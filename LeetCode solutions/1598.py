class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0 
        for action in logs:
            if '../' in action and count > 0:
                count -= 1
            if './' in action:
                continue
            else:
                count += 1

        return count