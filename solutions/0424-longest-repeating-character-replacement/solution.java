class Solution {
    public int characterReplacement(String s, int k) {
        int maxLength = 0;
        int left = 0;
        Map<Character, Integer> frequencyMap = new HashMap<>();
        int maxFrequency = 0; // Tracks the frequency of the most frequent character in the current window

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            frequencyMap.put(currentChar, frequencyMap.getOrDefault(currentChar, 0) + 1);
            maxFrequency = Math.max(maxFrequency, frequencyMap.get(currentChar));

            // Number of characters that need to be changed to make all characters in the window the same
            if ((right - left + 1) - maxFrequency > k) {
                char leftChar = s.charAt(left);
                frequencyMap.put(leftChar, frequencyMap.get(leftChar) - 1);
                left++;
            }

            // Update the maximum length of the substring found
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
