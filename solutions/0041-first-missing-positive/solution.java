class Solution {
    public int firstMissingPositive(int[] nums) {
        List<Integer> arr = new ArrayList<>();
        for (int num : nums) {
            arr.add(num);
        }
        Collections.sort(arr);
        int i = 1;
        for (int num : arr) {
            if (num == i) {
                i++;
            }
        }
        return i;
    }
}
