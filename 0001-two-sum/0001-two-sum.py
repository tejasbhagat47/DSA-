class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        
        
        dictt = {}

        for i in range(n):
            diff = target - nums[i]

            if diff in dictt:
                return [dictt[diff],i]
            
            dictt[nums[i]] = i

        
        