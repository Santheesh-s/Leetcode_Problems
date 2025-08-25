class Solution {
    public int maxCoins(int[] piles) {
        Arrays.sort(piles);
        int sum1=0,n=piles.length;
        for(int i=n/3;i<n;i+=2)
            sum1+=piles[i];
        return sum1;
    }
}
