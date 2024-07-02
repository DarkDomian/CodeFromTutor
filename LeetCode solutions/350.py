class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans = []

        if len(nums1) <= len(nums2):
            for num in set(nums1):
                if num in nums2:
                    for i in range(min(nums1.count(num), nums2.count(num))):
                        ans.append(num)
        else:
            for num in set(nums2):
                    for i in range(min(nums1.count(num), nums2.count(num))):
                        ans.append(num)

        return ans