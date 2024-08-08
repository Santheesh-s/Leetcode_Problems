class Solution {
    public int lengthOfLastWord(String s) {
        int len = 0;
        int i = 1;
        while (s.charAt(s.length() - i) == ' ') {
            i++;
        }
        for (int k = s.length() - i; k >= 0 && s.charAt(k) != ' '; k--) {
            len++;
        }

        return len;
    }
}
