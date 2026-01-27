class Solution {
    public long minCost(String s, int[] cost) {
        long arr[]=new long[26];
        long sum=0,max=0;
        int i=0;
        for(char a:s.toCharArray())
        {
            arr[a-'a']+=cost[i];
            sum+=cost[i];
            max=Math.max(arr[a-'a'],max);
            i++;
        }
        return (long)(sum-max);
    }
}
