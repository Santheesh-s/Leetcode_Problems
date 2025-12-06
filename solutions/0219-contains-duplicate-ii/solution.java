class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer,Integer>map=new HashMap<>();
        int n=nums.length;
        for(int i=0;i<n;i++)
        {
            if(map.containsKey(nums[i]))
            {
                int a=map.get(nums[i]);
                if(i-a<=k)
                    return true;
            }
            map.put(nums[i],i);
        }
        return false;
    }
}
