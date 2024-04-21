class Solution(object):
    def getConcatenation(self, nums):
        arr = []
        n=2*len(nums)
        for i in range(0, n, 1):
            arr.append(nums[i%len(nums)])
        return arr
            