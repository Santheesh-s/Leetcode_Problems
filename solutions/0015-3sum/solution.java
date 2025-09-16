class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n=nums.length;
        List<List<Integer>>ls=new ArrayList<>();
        for(int i=0;i<n-2;i++)
        {
            if(i>0 && nums[i]==nums[i-1])continue;
            int left=i+1,right=n-1;
            while(left<right)
            {
                int sum=nums[left]+nums[right]+nums[i];
                if(sum==0)
                {
                    ls.add(Arrays.asList(nums[left],nums[right],nums[i]));
                    left++;
                    right--;
                }
                else if(sum>0)
                    right--;
                else
                    left++;
            }
        }
        return new ArrayList<>(new HashSet<>(ls));
    }
}
