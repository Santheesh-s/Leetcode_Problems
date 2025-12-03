class Solution {
    public int subarraySum(int[] nums, int k) {
        int currentSum=0,n=nums.length,count=0;
        Map<Integer,Integer>map=new HashMap<>();
        map.put(0,1);
        for(int i=0;i<n;i++)
        {
            currentSum+=nums[i];
            if(map.containsKey(currentSum-k))
                count += map.get(currentSum - k);
            map.put(currentSum,map.getOrDefault(currentSum,0)+1);
        }
        return count;
    }
}
