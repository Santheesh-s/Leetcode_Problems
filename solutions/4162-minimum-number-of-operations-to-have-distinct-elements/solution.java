class Solution {
    public int minOperations(int[] nums) {
        Map<Integer,Integer>map=new HashMap<>();
        for(int i=nums.length-1;i>=0;i--)
        {
            if(map.containsKey(nums[i]))
                return (i+3)/3;
            map.put(nums[i],1);
        }
        return 0;
    }
}
