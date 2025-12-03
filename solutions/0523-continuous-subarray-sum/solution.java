class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int n=nums.length,currentSum=0;
        Map<Integer,Integer>map=new HashMap<>();
        map.put(0,-1);
        for(int i=0;i<n;i++)
        {
            currentSum+=nums[i];
            if(map.containsKey(currentSum%k) && i-map.get(currentSum%k)>=2)
                return true;
            if(!map.containsKey(currentSum%k))
                map.put(currentSum%k,i);
        }
        return false;
    }
}
