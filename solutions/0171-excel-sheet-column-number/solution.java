class Solution {
    public int titleToNumber(String c) {
        int result=0;
        for(char i:c.toCharArray())
            result = result * 26 + (i - 64);
        return result;
    }
}
