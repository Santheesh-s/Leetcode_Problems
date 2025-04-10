class Solution {
    public int maximumValue(String[] strs) {
        int n=0;
        for(String s:strs)
        {
            if(s != null && s.matches("\\d+"))
                n=Math.max(n,Integer.parseInt(s));
            else
                n=Math.max(n,s.length());
        }
        return n;
    }
}
