class Solution(object):
    def decompressRLElist(self, nums):
        output = []
        for i in range(0, len(nums),2):
            freq = nums[i]
            freq_list = []
            for j in range(nums[i]+1):
                freq_list.append(nums[i])
            for k in range(1, len(freq_list)):
                output.append(nums[i+1])
        return output
        