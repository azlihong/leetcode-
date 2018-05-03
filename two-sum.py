class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        # no special case handling becasue it's assumed that it has only one solution
a=[2,3,6,7]
taregt=9
A=Solution()
print(A.twoSum(a,taregt))