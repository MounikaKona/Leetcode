class Solution(object):
    def maximumWealth(self, accounts):
        arr = []
        for i in range(0, len(accounts), 1):
            x = sum(accounts[i])
            arr.append(x)
        return max(arr)