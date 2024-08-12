class Solution {
    public int[] sortArray(int[] nums) {
        List<Integer>ls=new ArrayList<>();
        for(int i=0;i<nums.length;i++)
            ls.add(nums[i]);
        Collections.sort(ls);
        return ls.stream().mapToInt(Integer::intValue).toArray();
    }
}
