class Solution {
    public int findDuplicate(int[] nums) {
        boolean[] array = new boolean[nums.length];
        for (int num : nums) {
            if (array[num])
                return num;
            array[num] = true;

        }
        return 0;
    }
}
