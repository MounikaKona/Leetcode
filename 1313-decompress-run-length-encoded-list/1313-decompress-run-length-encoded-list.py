class Solution(object):
    def decompressRLElist(self, nums):
        output = []
        for i in range(0, len(nums),2):
            freq = nums[i]
            value = nums[i+1]
            output.extend([value] * freq)
        return output
        