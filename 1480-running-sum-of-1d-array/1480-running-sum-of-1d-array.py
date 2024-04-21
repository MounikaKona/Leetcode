class Solution(object):
    def runningSum(self, nums):
        runningsum = []
        for i in range(1):
            x = nums[i]
            runningsum.append(x)
            for j in range(i+1, len(nums), 1):
                x = x+nums[j]
                runningsum.append(x)
        return runningsum
            
        