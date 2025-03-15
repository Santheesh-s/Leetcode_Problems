class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n=max(candies)
        return [True  if i+extraCandies>=n else False for i in candies]
