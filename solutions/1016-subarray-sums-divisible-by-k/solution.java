class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        Map<Integer,Integer>map=new HashMap<>();
        int currentSum=0,count=0,n=nums.length;
        map.put(0,1);
        for(int i=0;i<n;i++)
        {
            currentSum+=nums[i];
            int mod = ((currentSum % k) + k) % k;
            if(map.containsKey(mod))
                count+=map.get(mod);
            map.put(mod,map.getOrDefault(mod,0)+1);
        }
        return count;
    }
}
