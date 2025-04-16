class Solution {
    public boolean isPalindrome(int x) {
        String a=String.valueOf(x);
        StringBuilder sc=new StringBuilder(a);
        return sc.reverse().toString().equals(a);
    }
}
