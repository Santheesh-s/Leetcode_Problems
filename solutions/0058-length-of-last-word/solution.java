class Solution {
    public int lengthOfLastWord(String s) {
        int i=0;
        for(i=s.length()-1;i>=0 && s.charAt(i)==' ';i--);
        int l=0;
        if(i>=0)
            while(i>=0 && s.charAt(i)!=' ')
            {    l++;i--; }
        
        return l;
    }
}
