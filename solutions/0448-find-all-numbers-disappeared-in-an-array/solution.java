import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> missingNumbers = new ArrayList<>();
        
        // Mark each number as found by negating the value at the corresponding index
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;
            if (nums[index] > 0) {
                nums[index] = -nums[index]; // Mark as found
            }
        }

        // Add the missing numbers (those whose indices are still positive)
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                missingNumbers.add(i + 1); // i + 1 because numbers are from 1 to n
            }
        }

        return missingNumbers;
    }
}

