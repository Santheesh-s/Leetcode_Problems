class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        int majorityElement = nums[0];
        int maxFrequency = 0;

        // Populate the frequency map
        for (int i = 0; i < nums.length; i++) {
            int count = freq.getOrDefault(nums[i], 0) + 1;
            freq.put(nums[i], count);

            // Update the majority element if current element has a higher frequency
            if (count > maxFrequency) {
                maxFrequency = count;
                majorityElement = nums[i];
            }
        }

        return majorityElement;
    }
}

