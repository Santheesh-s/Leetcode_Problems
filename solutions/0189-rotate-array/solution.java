class Solution {
    public void rotate(int[] nums, int k) {
        List<Integer>alist= new ArrayList<>();
        for(int i=0;i<nums.length;i++)
        {
            alist.add(nums[i]);
        }
        Collections.rotate(alist,k);
        for (int i = 0; i < nums.length; i++) {
            nums[i] = alist.get(i);
        }

        System.out.println(Arrays.toString(nums)); 
    }
}
