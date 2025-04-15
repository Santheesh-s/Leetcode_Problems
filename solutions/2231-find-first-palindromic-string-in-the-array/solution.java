class Solution {
    public String firstPalindrome(String[] words) {
        for(String a:words)
        {
            StringBuilder sc=new StringBuilder(a);
            sc.reverse();
            if(sc.toString().equals(a))
                return sc.toString();
        }
        return "";
    }
}
