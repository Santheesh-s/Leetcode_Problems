class Solution {
    public int maxProfit(int[] prices) {
    int m=prices[0],profit=0;
    for(int i=1;i<prices.length;i++)
    {
        if(prices[i]<m)
            m=prices[i];
        else
            profit=Math.max(profit,prices[i]-m);
        
    }
    return profit;
    }
}
