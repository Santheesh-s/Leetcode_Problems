class Solution {
    public boolean isStrictlyPalindromic(int n) {
        for(int i=2;i<=n-2;i++)
        {
            String str = Integer.toString(n,i);
            if(!isPalindrome(str))
                return false;
        }
        return true;
    }
    public static boolean isPalindrome(String str) {
        return str.equals(new StringBuilder(str).reverse().toString());
    }
}
