class Solution(object):
    def numberGame(self, nums):
        arr = []
        nums.sort()
        for i in range(0, len(nums), 2):
            print(nums[i])
            print(nums[i+1])
            arr.append(nums[(i+1)])
            arr.append(nums[i])
        return arr
        