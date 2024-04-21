class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = []
        for i in range(0, len(nums), 1):
            count = 0
            for j in range(len(nums)-1, -1, -1):
                if nums[j] < nums[i]:
                    count +=1
            arr.append(count)
        return arr
         