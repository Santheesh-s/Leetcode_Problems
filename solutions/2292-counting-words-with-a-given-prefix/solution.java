class Solution {
    public int prefixCount(String[] words, String pref) {
        int n=0;
        for(String a:words)
        {
            if(a.startsWith(pref))
                n++;
        }
        return n;
    }
}
