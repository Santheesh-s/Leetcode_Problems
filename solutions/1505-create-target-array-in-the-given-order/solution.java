class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        List<Integer> ls=new ArrayList<>();
        for(int i=0;i<index.length;i++)
            ls.add(index[i],nums[i]);
        int a=0;
        for(int n:ls)
            nums[a++]=n;
        return nums;
    }
}
