class Solution {
    public String reversePrefix(String word, char ch) {
        String s="";
        int o=0;
        char[] word1=word.toCharArray();
        for(int i=0;i<word1.length;i++)
        {
            s+=word1[i];
            if(o==0 && word1[i]==ch)
            {
                s=new StringBuilder(s).reverse().toString();
                o=1;
            }
        }
        return s.toString();
    }
}
