class Solution {
    public int countOdds(int low, int high) {
        if (low % 2 == 0) {
            low++;
        }

        // If high is odd, include it in the count, else end at the previous odd number
        if (high % 2 == 0) {
            high--;
        }

        // Calculate the number of odd numbers between low and high inclusive
        if (low > high) {
            return 0; // No odd numbers in the range
        }

        return (high - low) / 2 + 1;
    }
}
