class Solution {
    public String customSortString(String order, String s) {
        String ls="";
        for(char i:order.toCharArray())
        {
            if(s.contains(i+""))
            {
                ls+=(i+"").repeat(count(s,i));
                s=s.replace(i+"","");
            }
        }
        return ls+s;
    }
    int count(String s,char i)
    {
        int n=s.length();
        s=s.replace(i+"","");
        return n-s.length();
    }
}
