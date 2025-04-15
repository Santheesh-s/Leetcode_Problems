class Solution {
    public boolean isCircularSentence(String sentence) {
        String[] ls=sentence.split("\\ ");
        int n=ls.length;
        for(int i=1;i<n;i++)
        {
            if(ls[i].charAt(0)!=ls[i-1].charAt(ls[i-1].length()-1))
                return false;
        }
        return ls[0].charAt(0)==ls[n-1].charAt(ls[n-1].length()-1);
    }
}
