class Solution(object):
    def countPairs(self, nums, target):
        count = 0
        for i in range(0, len(nums), 1):
            for j in range(i+1, len(nums),1):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
        