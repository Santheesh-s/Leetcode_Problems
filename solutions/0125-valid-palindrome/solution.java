class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        char str[]=new char[s.length()];
        int k=0;
        for (char c : s.toCharArray()) 
        {
            if (Character.isLetterOrDigit(c))
            {
                str[k++]=c;
            }
        }
        int left=0,right=k-1;
        while (left < right) {
            if (str[left] != str[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
