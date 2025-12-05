class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n=nums.length;
        List<Integer>ls=new ArrayList<>();
        for(int i=0;i<n;i++)
        {
            int id=Math.abs(nums[i])-1;
            if(nums[id]>0)
                nums[id]=-nums[id];
        }
        for(int i=0;i<n;i++)
            if(nums[i]>0)
                ls.add(i+1);
        return ls;
        
    }
}
