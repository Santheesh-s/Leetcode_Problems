class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String s1="",s2="";
        for(String a:word1)
            s1+=a;
        for(String a:word2)
            s2+=a;
        return s1.equals(s2);
    }
}
