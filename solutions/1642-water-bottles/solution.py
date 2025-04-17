class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        sum=numBottles;
        while(numBottles>=numExchange):
            sum+=numBottles/numExchange;
            numBottles=numBottles/numExchange+(numBottles%numExchange);
        return sum;
