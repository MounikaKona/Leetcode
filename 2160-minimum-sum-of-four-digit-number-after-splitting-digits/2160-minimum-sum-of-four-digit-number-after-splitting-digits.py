class Solution(object):
    def minimumSum(self, num):
        num = str(num)
        num = list(num)
        num.sort()
        firsthalf = num[0:2]
        secondhalf = num[2: ]
        new1 = int(min(firsthalf) + min(secondhalf))
        new2 = int(max(firsthalf) + max(secondhalf))
        output = new1+new2
        return output