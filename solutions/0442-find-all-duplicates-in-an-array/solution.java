class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> ls=new ArrayList<>();
        int n=nums.length;
        for(int i=0;i<n;i++)
        {
            int id = Math.abs(nums[i]) - 1;
            if(nums[id]<0) 
                ls.add(Math.abs(nums[i]));
            else
                nums[id]=-nums[id];
        }
        return ls;
    }
}
