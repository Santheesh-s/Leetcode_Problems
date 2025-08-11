class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int tot=0,count=0;
        for(int i=0;i<costs.length;i++)
        {
            tot+=costs[i];
            if(tot>coins)
                return count;
            count++;
        }
        return count;
    }
}
