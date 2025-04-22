int maxProfit(int* prices, int n) {
    int m=prices[0],profit=0;
    for(int i=1;i<n;i++)
    {
        if(prices[i]<m)
            m=prices[i];
        else
            profit=fmax(profit,prices[i]-m);
        
    }
    return profit;
}
