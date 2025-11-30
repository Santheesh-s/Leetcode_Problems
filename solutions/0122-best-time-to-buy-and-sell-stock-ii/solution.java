class Solution {
    public int maxProfit(int[] prices) {
        int min=prices[0],profit=0,i=0;
        while(i<prices.length)
        {
            if(prices[i]>min)
                profit+=prices[i]-min;
            min=prices[i];
            i++;
        }
        return profit;
    }
}
