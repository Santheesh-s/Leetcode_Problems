class Solution {
    public int[] numberOfLines(int[] width, String s) {
        int line=0,p=0,k=0;
        for(char a:s.toCharArray())
        {
            if(p+width[a-97]>100)
            {
                line++;
                p=0;
            }
            p+=width[a-97];
        }
        return new int[] {line+1,p};
    }
}
