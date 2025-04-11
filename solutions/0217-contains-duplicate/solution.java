class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer>ls=new HashSet<>();
        int i=0;
        for(int n:nums)
        {
            if(!ls.add(n))
            {
                i=1;
                break;
            }
        }
        if(i!=0)
            return true;
        return false;
    }
}
