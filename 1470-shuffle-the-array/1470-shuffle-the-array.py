class Solution(object):
    def shuffle(self, nums, n):
        arr = []
        for i in range(0, n, 1):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr
        