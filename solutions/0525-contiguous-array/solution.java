class Solution {
    public int findMaxLength(int[] nums) {
        int n=nums.length,maxLength=0,currentSum=0;
        Map<Integer,Integer>map=new HashMap<>();
        map.put(0,-1);
        for(int i=0;i<n;i++)
        {
            currentSum+=(nums[i]==1)?1:-1;
            if(map.containsKey(currentSum))
                maxLength=Math.max(maxLength,i-map.get(currentSum));
            else
                map.put(currentSum,i);
        }
        return maxLength;
    }
}
