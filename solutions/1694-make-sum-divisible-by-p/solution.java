class Solution {
    public int minSubarray(int[] nums, int p) {
        Map<Integer,Integer>map=new HashMap<>();
        int currentSum=0,rem=0,n=nums.length;
        int length=n;
        long sum=0;
        for(int i:nums)
            sum+=i;
        rem=(int)(sum%p);
        if(rem==0) return 0;
        map.put(0,-1);
        for(int i=0;i<n;i++)
        {
            currentSum = (currentSum + nums[i]) % p;
            int key = (currentSum - rem)% p;
            if (key < 0) key += p;
            if(map.containsKey(key))
                length=Math.min(length,i-map.get(key));
            map.put(currentSum, i);
        }
        return length == n ? -1 : length;
    }
}
