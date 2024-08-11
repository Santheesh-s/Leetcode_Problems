class Solution {
    public int missingNumber(int[] nums) {
        List<Integer>ls=new ArrayList<>();
        for(int n:nums)
            ls.add(n);
        for(int i=0;i<=nums.length;i++)
        {
            if(!ls.contains(i))
                return i;
        }
        return 0;
    }
}
