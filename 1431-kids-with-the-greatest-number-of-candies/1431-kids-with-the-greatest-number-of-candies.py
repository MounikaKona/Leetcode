class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        x=max(candies)
        for i in range(0, len(candies), 1):
            y = candies[i] + extraCandies
            if y >= x:
                result.append(True)
            else:
                result.append(False)
        return(result)
        